#!/usr/bin/env python3
import hashlib, io, json, math, tarfile, urllib.request
from collections import Counter
import pymupdf
from shapely.geometry import Polygon, MultiPolygon, GeometryCollection, box, LineString
from shapely.ops import unary_union

SOURCE_URL="https://export.arxiv.org/e-print/2308.07955v2"
SOURCE_SHA256="484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c"
ASSETS={
 "Majorana":("Presentation/CnstrntPlotMajoranaNeff.pdf","8b5c5839fada534ed10d79768335050814765a6ec00bddcb51e75cc0f64e7837"),
 "Dirac":("Presentation/CnstrntPlotDiracNeff.pdf","c06b66e5cb35c3b1cae341da393e9b638d3f3f536cef09a3ca5431600fb2ed4a"),
}
# Exact source-native PDF RGB tuples observed in 0080a and tied to the primary
# caption color names. No nearest-color matching is allowed.
DARK_BLUE=(0.0,0.46666,0.733322)
LIGHT_BLUE=(0.199997,0.733322,0.933319)
GREEN=(0.0,0.599991,0.533325)
FORBIDDEN={(0.933319,0.199997,0.46666),(0.799988,0.199997,0.066666),(0.933319,0.46666,0.199997),GREEN}
AX=0.014151317772708815; BX=-6.9932501456724525
AY=-0.0329969798924973; BY=-2.6510803066554596
PHYS_BOX=box(-9.0,-17.0,0.0,-3.0)

def sha256(b): return hashlib.sha256(b).hexdigest()
def ck(c): return None if c is None else tuple(round(float(x),6) for x in c)
def pxy(p): return (float(p.x),float(p.y))
def dist(a,b): return math.hypot(a[0]-b[0],a[1]-b[1])

def cubic(p0,p1,p2,p3,t):
 u=1-t
 return (u**3*p0[0]+3*u*u*t*p1[0]+3*u*t*t*p2[0]+t**3*p3[0],u**3*p0[1]+3*u*u*t*p1[1]+3*u*t*t*p2[1]+t**3*p3[1])

def point_line_distance(p,a,b):
 vx,vy=b[0]-a[0],b[1]-a[1]; wx,wy=p[0]-a[0],p[1]-a[1]
 vv=vx*vx+vy*vy
 if vv==0:return dist(p,a)
 t=max(0,min(1,(wx*vx+wy*vy)/vv)); q=(a[0]+t*vx,a[1]+t*vy)
 return dist(p,q)

def flatten_cubic(p0,p1,p2,p3,tol,depth=0):
 if max(point_line_distance(p1,p0,p3),point_line_distance(p2,p0,p3))<=tol or depth>=24:
  return [p0,p3]
 l01=((p0[0]+p1[0])/2,(p0[1]+p1[1])/2); l12=((p1[0]+p2[0])/2,(p1[1]+p2[1])/2); l23=((p2[0]+p3[0])/2,(p2[1]+p3[1])/2)
 l012=((l01[0]+l12[0])/2,(l01[1]+l12[1])/2); l123=((l12[0]+l23[0])/2,(l12[1]+l23[1])/2); mid=((l012[0]+l123[0])/2,(l012[1]+l123[1])/2)
 a=flatten_cubic(p0,l01,l012,mid,tol,depth+1); b=flatten_cubic(mid,l123,l23,p3,tol,depth+1)
 return a[:-1]+b

def rings_from_drawing(d,tol):
 rings=[]; cur=[]
 def add(pt):
  nonlocal cur
  if not cur or dist(cur[-1],pt)>1e-9: cur.append(pt)
 def flush():
  nonlocal cur
  if len(cur)>=3:
   if dist(cur[0],cur[-1])>1e-7: cur.append(cur[0])
   if len(cur)>=4: rings.append(cur)
  cur=[]
 for it in d.get('items',[]):
  op=it[0]
  if op=='l':
   a,b=pxy(it[1]),pxy(it[2])
   if cur and dist(cur[-1],a)>1e-6: flush()
   add(a); add(b)
  elif op=='c':
   pts=[pxy(x) for x in it[1:5]]
   if cur and dist(cur[-1],pts[0])>1e-6: flush()
   seg=flatten_cubic(*pts,tol)
   for q in seg:add(q)
  elif op=='re':
   flush(); r=it[1]; rings.append([(r.x0,r.y0),(r.x1,r.y0),(r.x1,r.y1),(r.x0,r.y1),(r.x0,r.y0)])
  elif op=='qu':
   flush(); q=it[1]; rings.append([pxy(q.ul),pxy(q.ur),pxy(q.lr),pxy(q.ll),pxy(q.ul)])
 flush()
 return rings

def filled_geom(d,tol):
 rings=rings_from_drawing(d,tol)
 polys=[]
 for r in rings:
  try:
   p=Polygon(r)
   if p.is_valid and p.area>1e-12: polys.append(p)
  except Exception: pass
 if not polys:return GeometryCollection(),rings
 # PDF contourf paths are emitted using even-odd fill where nested subpaths
 # occur. Apply exact even-odd parity; otherwise preserve native nonzero fill
 # conservatively through union. No topology repair is used.
 if bool(d.get('even_odd')):
  g=GeometryCollection()
  for p in polys: g=p if g.is_empty else g.symmetric_difference(p)
 else:
  g=unary_union(polys)
 return g,rings

def to_phys_xy(x,y): return (AX*x+BX-3.0, AY*y+BY)
def to_pdf_xy(lm,lg): return ((lm+3.0-BX)/AX,(lg-BY)/AY)
def transform_geom(g):
 from shapely.ops import transform
 return transform(lambda x,y,z=None:(AX*x+BX-3.0,AY*y+BY),g)

def iter_polys(g):
 if isinstance(g,Polygon): return [g]
 if isinstance(g,MultiPolygon): return list(g.geoms)
 return [x for x in getattr(g,'geoms',[]) if isinstance(x,Polygon)]

def boundary_native_control(g_phys,native_lines):
 # Controls are sampled only from non-clipping boundary points. Clipping-box
 # edges are an explicitly allowed operation in the prereg and are not native
 # contour paths.
 vals=[]
 minx,miny,maxx,maxy=PHYS_BOX.bounds
 for p in iter_polys(g_phys):
  coords=list(p.exterior.coords)
  step=max(1,len(coords)//50)
  for lm,lg in coords[::step]:
   if min(abs(lm-minx),abs(lm-maxx),abs(lg-miny),abs(lg-maxy))<1e-8: continue
   x,y=to_pdf_xy(lm,lg)
   vals.append(min(line.distance(pymupdf.Point(x,y)) if False else LineString(line.coords).distance(__import__('shapely').geometry.Point(x,y)) for line in native_lines))
 return vals

def inspect_scenario(pdf_bytes,name,tol):
 doc=pymupdf.open(stream=pdf_bytes,filetype='pdf'); page=doc[0]; drawings=page.get_drawings()
 fill_counts=Counter(ck(d.get('fill')) for d in drawings if d.get('fill') is not None)
 selected=[]; forbidden_ids=[]
 for i,d in enumerate(drawings):
  c=ck(d.get('fill'))
  if c in (DARK_BLUE,LIGHT_BLUE): selected.append((i,c,d))
  if c in FORBIDDEN: forbidden_ids.append((i,c))
 if not selected:
  return {'scenario':name,'classification':'BLOCKED_COSMOLOGY_B_L_CMB_VECTOR_COLOR_IDENTITY','reason':'no exact native light/dark-blue fill objects'}
 pieces=[]; lines=[]; ids=[]
 for i,c,d in selected:
  g,rings=filled_geom(d,tol); ids.append({'drawing_id':i,'fill':c,'ring_count':len(rings),'even_odd':bool(d.get('even_odd'))})
  if not g.is_empty: pieces.append(g)
  for r in rings:
   if len(r)>=2: lines.append(LineString(r))
 if not pieces:
  return {'scenario':name,'classification':'SCIENTIFIC_FAIL_COSMOLOGY_B_L_CMB_EXCLUDED_GEOMETRY','reason':'selected native objects yielded no valid polygon'}
 pdf_union=unary_union(pieces)
 phys=transform_geom(pdf_union).intersection(PHYS_BOX)
 polys=iter_polys(phys)
 valid=bool(polys) and all(p.is_valid for p in polys) and phys.area>0
 controls=boundary_native_control(phys,lines) if lines else []
 return {'scenario':name,'classification':'candidate','fill_color_counts':{str(k):v for k,v in fill_counts.items()},'selected':ids,'forbidden_fill_object_count':len(forbidden_ids),'component_count':len(polys),'valid':valid,'area_decade2':phys.area,'bounds':list(phys.bounds) if not phys.is_empty else None,'boundary_control_count':len(controls),'boundary_control_max_pt':max(controls) if controls else 0.0,'geometry_wkt':phys.wkt}

def fetch_source():
 req=urllib.request.Request(SOURCE_URL,headers={'User-Agent':'NMIR-CMB-geometry/0080d'})
 with urllib.request.urlopen(req,timeout=90) as r:return r.read()

def audit():
 raw=fetch_source(); h=sha256(raw)
 if h!=SOURCE_SHA256: raise RuntimeError(f'source SHA mismatch {h}')
 blobs={}
 with tarfile.open(fileobj=io.BytesIO(raw),mode='r:*') as tf:
  mm={m.name.lstrip('./'):m for m in tf.getmembers() if m.isfile()}
  for sc,(path,expected) in ASSETS.items():
   if path not in mm: raise RuntimeError(f'missing {path}')
   data=tf.extractfile(mm[path]).read()
   if sha256(data)!=expected: raise RuntimeError(f'PDF SHA mismatch {path}')
   blobs[sc]=data
 out={'iteration':'0080d','source_sha256':SOURCE_SHA256,'tolerances_pt':{'base':0.02,'refined':0.01},'scenarios':{},'guard':'Hard CMB DeltaNeff>=0.4 geometry only; scenarios separate; no raster/manual input, green inclusion, topology repair, envelope union or response scan.'}
 allpass=True
 for sc,data in blobs.items():
  b=inspect_scenario(data,sc,0.02); r=inspect_scenario(data,sc,0.01)
  if b.get('classification','').startswith('BLOCKED') or r.get('classification','').startswith('BLOCKED'):
   out['scenarios'][sc]={'base':b,'refined':r}; allpass=False; continue
  ar=r['area_decade2']; ad=abs(b['area_decade2']-ar)/ar if ar>0 else math.inf
  from shapely import wkt
  gb=wkt.loads(b['geometry_wkt']); gr=wkt.loads(r['geometry_wkt']); sd=gb.symmetric_difference(gr).area/ar if ar>0 else math.inf
  checks={'nonzero_area':ar>0,'valid':b['valid'] and r['valid'],'area_refinement_rel':ad,'area_refinement_pass':ad<=0.005,'symdiff_refinement_rel':sd,'symdiff_refinement_pass':sd<=0.005,'boundary_control_max_pt':r['boundary_control_max_pt'],'boundary_control_pass':r['boundary_control_max_pt']<=0.02,'selected_only_allowed_colors':all(tuple(x['fill']) in (DARK_BLUE,LIGHT_BLUE) for x in r['selected'])}
  spass=all([checks['nonzero_area'],checks['valid'],checks['area_refinement_pass'],checks['symdiff_refinement_pass'],checks['boundary_control_pass'],checks['selected_only_allowed_colors']])
  allpass &= spass
  for x in (b,r): x.pop('geometry_wkt',None)
  out['scenarios'][sc]={'base':b,'refined':r,'checks':checks,'pass':spass}
 blocked=any(v['base'].get('classification','').startswith('BLOCKED') or v['refined'].get('classification','').startswith('BLOCKED') for v in out['scenarios'].values())
 out['classification']='BLOCKED_COSMOLOGY_B_L_CMB_VECTOR_COLOR_IDENTITY' if blocked else ('PASS_COSMOLOGY_B_L_CMB_CONSERVATIVE_EXCLUDED_GEOMETRY' if allpass else 'SCIENTIFIC_FAIL_COSMOLOGY_B_L_CMB_EXCLUDED_GEOMETRY')
 return out

def main():
 r=audit()
 with open('esseili_kribs_cmb_excluded_0080d.json','w') as f: json.dump(r,f,indent=2,sort_keys=True); f.write('\n')
 print(json.dumps(r,indent=2,sort_keys=True))
 if r['classification']!='PASS_COSMOLOGY_B_L_CMB_CONSERVATIVE_EXCLUDED_GEOMETRY': raise SystemExit(2)
if __name__=='__main__': main()
