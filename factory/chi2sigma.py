import gen as g
from gen import f2s, ujsor, mujsor, frac, br, cbr

import numpy as np
from scipy.stats import chi2

def chi2crit(p,df):
   return(r'\chi^2_'+cbr(f2s(p,3)+r',\ df='+str(df))+'='+f2s(chi2.ppf(p,df),3))
   #return( r'\chi^2_{{{{a}}},{{{df}}}}={ta}'.format(df=df, a=f2s(p,3), ta=f2s(chi2.ppf(p,df),3)))

d=dict()
def init(inp):
   global d
   d=inp
   if 'jelleg' in d:
      d['hip']=g.sigmahip(j=g.jellegT[d['jelleg']], sigma0=d['sigma0'])
   X=np.array(d['X'])
   n=d['n']=len(X)
   df=n-1
   d['sumval']=np.sum(X)
   d['sumjel']=g.sumjel(X[0], X[n-1])
   d['meanval']=d['mu']
   d['meanjel']=f2s(d['meanval'])
   #d['diffval']=d['meanval']-d['mu0']
   #d['diffjel']=r'{mean}-{mu0}'.format(mean=f2s(d['meanval']), mu0=f2s(d['mu0']))
   d['sum2jel']=g.sum2jel(X[0], X[n-1], d['meanval'])
   d['sum2val']=np.sum((X-d['meanval'])**2)
   d['sjel']=br(frac(d['sum2jel'], str(df)))+r'^\frac{1}{2}'
   d['sval']=np.std(X,ddof=1)
   #d['errval']=d['sval']/np.sqrt(n)
   #d['errjel']=f2s(d['errval'])
   d['chi2val']=df*(d['sval']/d['sigma0'])**2
   d['chi2jel']=str(df)+br(frac(f2s(d['sval']), f2s(d['sigma0'])))+r'^2'
   alfa=d['alfa']
   d['krit']=[chi2crit(1-alfa,df), chi2crit(1-0.5*alfa,df), \
   chi2crit(alfa,df), chi2crit(0.5*alfa,df)]



def perform():
   out=r'1-mintás $\chi^2$-próba\newline'+ujsor
   out+=r'\Mat{'+ujsor
   n=d['n']
   out+=r'n={n}'.format(n=n)+mujsor
   out+=r's = '+d['sjel']+' = '+mujsor
   out+=r' = '+br(frac(f2s(d['sum2val']),str(n-1)))+r'^{\frac{1}{2}}'
   out+=r' = {s}'.format(s=f2s(d['sval']))+mujsor
   out+=r'\chi^2 = '+d['chi2jel']+' = '+f2s(d['chi2val'])+mujsor
   out+=d['krit'][0]+r'\hspace{1cm}'+d['krit'][1]+mujsor
   out+=d['krit'][2]+r'\hspace{1cm}'+d['krit'][3]
   print(out+'\n'+r'}'+ujsor)
