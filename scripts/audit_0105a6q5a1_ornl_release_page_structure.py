#!/usr/bin/env python3
import argparse, hashlib, json, re, urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

PREREG='f0c211182f71d7b27f3093e15ce29646072f5582'
URL='https://coherent.ornl.gov/data-releases/'

class P(HTMLParser):
    def __init__(self): super().__init__(); self.a=[]; self.cur=None
    def handle_starttag(self, tag, attrs):
        if tag.lower()=='a': self.cur={'href':dict(attrs).get('href',''),'text':[]}
    def handle_data(self, data):
        if self.cur is not None: self.cur['text'].append(data)
    def handle_endtag(self, tag):
        if tag.lower()=='a' and self.cur is not None:
            self.a.append({'href':self.cur['href'],'text':' '.join(''.join(self.cur['text']).split())}); self.cur=None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); args=ap.parse_args()
    out={'gate':'NMIR-V2-0105A6Q5A1','preregistration_commit':PREREG,'git_sha':args.git_sha,
         'linked_resources_followed':False,'scientific_release_content_inspected':False,'pseudo_data_generated':False,
         'likelihood_evaluated':False,'observed_bsm_residual_inspected':False,
         'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,
         'observed_bsm_residual_permission_percent':0}
    try:
        req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-provenance-audit/1.0'})
        with urllib.request.urlopen(req,timeout=30) as r:
            b=r.read(); final=r.geturl(); status=getattr(r,'status',200); ctype=r.headers.get('Content-Type','')
        out['provider']={'requested_url':URL,'final_url':final,'status':status,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'content_type':ctype}
        if status!=200: raise RuntimeError(f'HTTP {status}')
        p=P(); p.feed(b.decode('utf-8','replace'))
        filt=[]
        for i,a in enumerate(p.a):
            href=a['href']; text=a['text']; resolved=urljoin(final,href); u=urlparse(resolved)
            target=bool(re.search(r'/records?/3903810(?:$|[/?#])',u.path + (('?' + u.query) if u.query else '') + (('#'+u.fragment) if u.fragment else '')))
            zhost=u.hostname in {'zenodo.org','www.zenodo.org'}
            flags={'text_has_data_release':'data release' in text.lower(),'text_has_argon':'argon' in text.lower(),'href_targets_3903810':target,'href_is_zenodo':zhost}
            if target or flags['text_has_data_release'] or flags['text_has_argon']:
                filt.append({'index':i,'text':text,'href':href,'resolved_hostname':u.hostname,'resolved_path':u.path,'resolved_query':u.query,'resolved_fragment':u.fragment,**flags})
        out['total_anchor_count']=len(p.a); out['filtered_anchors']=filt
        n=sum(1 for a in filt if a['href_targets_3903810'] and a['href_is_zenodo'])
        out['zenodo_3903810_anchor_count']=n
        out['classification']='PASS_0105A6Q5A1_ORNL_ZENODO_3903810_LINK_STRUCTURALLY_PRESENT_NONDISCOVERY' if n else 'BLOCKED_0105A6Q5A1_ORNL_ZENODO_3903810_LINK_NOT_PRESENT'
    except Exception as e:
        out['error']=f'{type(e).__name__}: {e}'; out['classification']='BLOCKED_0105A6Q5A1_ORNL_PAGE_TRANSPORT_FAILURE'
    raw=json.dumps(out,sort_keys=True,indent=2).encode(); open(args.output,'wb').write(raw+b'\n')
    print('CLASSIFICATION='+out['classification']); print('RESULT_SHA256='+hashlib.sha256(raw+b'\n').hexdigest())
if __name__=='__main__': main()
