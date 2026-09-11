#!/usr/bin/env python3
import argparse, hashlib, html, json, re, urllib.parse, urllib.request
from html.parser import HTMLParser
from pathlib import Path

PREREG='a55e26040be8fdd059563781d5a3a8c5ba1ed259'
SOURCES={
 'plaque':('https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html',23370,'f1c245e9675c1a533bc9ad03ca928820499381d576c5f6fefee59c33b91d7488'),
 'education':('https://ceem.indiana.edu/education/index.html',67845,'3de3e09e5ebdb4006c0d8b969c3f73a25b041b31534476b6bf6987bbf5591fe6'),
}
LITERALS=['dissertation','thesis','scholarworks','.pdf','download','benjamin suh','benjamin d. suh','towards an improved measurement of the cevns process with the cen...']
PASS='PASS_0105A6Q4FS_INSTITUTIONAL_DISSERTATION_LINK_CANDIDATES_LOCATED_NONDISCOVERY'
EMPTY='BLOCKED_0105A6Q4FS_NO_INSTITUTIONAL_DISSERTATION_LINK_CANDIDATES'
TRANSPORT='BLOCKED_0105A6Q4FS_SOURCE_TRANSPORT_FAILURE'
MISMATCH='FAIL_0105A6Q4FS_SOURCE_BYTE_IDENTITY_MISMATCH'

class Links(HTMLParser):
 def __init__(self): super().__init__(convert_charrefs=True); self.items=[]; self.cur=None
 def handle_starttag(self,tag,attrs):
  if tag.lower()=='a':
   href=dict(attrs).get('href')
   if href is not None: self.cur={'href':href,'text':[]}
 def handle_data(self,data):
  if self.cur is not None: self.cur['text'].append(data)
 def handle_endtag(self,tag):
  if tag.lower()=='a' and self.cur is not None:
   self.items.append({'href':self.cur['href'],'anchor':' '.join(''.join(self.cur['text']).split())}); self.cur=None

def candidate(url,anchor):
 s=(url+' '+anchor).casefold()
 if any(x in s for x in ['dissertation','thesis','scholarworks','.pdf','download','benjamin suh','benjamin d. suh']): return True
 title='towards an improved measurement of the cevns process with the cen...'
 if title in s: return True
 u=urllib.parse.urlparse(url.casefold()); toks=[t for t in re.split(r'[^a-z0-9]+',(u.netloc+u.path)) if t]
 return 'irem' in toks or 'ir' in toks

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
 out={'gate':'NMIR-V2-0105A6Q4FS','preregistration_commit':PREREG,'git_sha':a.git_sha,'page_links_followed':False,'pdf_downloaded':False,'pdf_content_inspected':False,'likelihood_evaluated':False,'pseudo_data_generated':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'observed_bsm_residual_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0}
 inventory=[]; probes={}
 try:
  for key,(url,size,sha) in SOURCES.items():
   req=urllib.request.Request(url,headers={'User-Agent':'NMIR-q4fs-link-locator/1.0'})
   with urllib.request.urlopen(req,timeout=90) as r: raw=r.read(); status=int(getattr(r,'status',r.getcode())); final=r.geturl()
   got=hashlib.sha256(raw).hexdigest(); probes[key]={'requested_url':url,'final_url':final,'status':status,'bytes':len(raw),'sha256':got}
   if status!=200: out['classification']=TRANSPORT; break
   if len(raw)!=size or got!=sha: out['classification']=MISMATCH; break
   p=Links(); p.feed(raw.decode('utf-8',errors='replace'))
   for x in p.items:
    absu=urllib.parse.urljoin(final,html.unescape(x['href']))
    inventory.append({'source':key,'raw_href':x['href'],'absolute_url':absu,'anchor_text':x['anchor'],'dissertation_link_candidate':candidate(absu,x['anchor'])})
  else:
   can=[x for x in inventory if x['dissertation_link_candidate']]
   canon=json.dumps(inventory,sort_keys=True,separators=(',',':')).encode()
   out['all_link_count']=len(inventory); out['all_link_inventory_sha256']=hashlib.sha256(canon).hexdigest(); out['candidate_count']=len(can); out['candidates']=can
   out['classification']=PASS if can else EMPTY
 except Exception as e:
  out['error']=type(e).__name__+': '+str(e); out['classification']=TRANSPORT
 out['probes']=probes
 Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print('CLASSIFICATION='+out['classification']); print('CANDIDATE_COUNT='+str(out.get('candidate_count',0)))
if __name__=='__main__': main()
