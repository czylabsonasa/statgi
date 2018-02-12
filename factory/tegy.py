import gen as g
from gen import f2s, ujsor, mujsor, frac, br, cbr

import numpy as np
from scipy.stats import t

def tcrit(p,df):
   return( r't^{{({df})}}_{{{a}}}={ta}'.format(df=df, a=f2s(p,3), ta=f2s(t.ppf(p,df),3)))

d=dict()
def init(inp):
   global d
   d=inp
   if 'jelleg' in d:
      d['hip']=g.muhip(j=g.jellegT[d['jelleg']], mu0=d['mu0'])
   X=np.array(d['X'])
   n=d['n']=len(X)
   df=n-1
   d['sumval']=np.sum(X)
   d['sumjel']=g.sumjel(X[0], X[n-1])
   d['meanval']=np.mean(X)
   d['meanjel']=frac(d['sumjel'], str(n))
   d['diffval']=d['meanval']-d['mu0']
   d['diffjel']=r'{mean}-{mu0}'.format(mean=f2s(d['meanval']), mu0=f2s(d['mu0']))
   d['sum2jel']=g.sum2jel(X[0], X[n-1], d['meanval'])
   d['sum2val']=np.sum((X-d['meanval'])**2)
   d['sjel']=br(frac(d['sum2jel'], str(df)))+r'^\frac{1}{2}'
   d['sval']=np.std(X,ddof=1)
   d['errval']=d['sval']/np.sqrt(n)
   d['errjel']=f2s(d['errval'])
   d['tval']=d['diffval']/d['errval']
   d['tjel']=frac(d['diffjel'], d['errjel'])+'='+\
   frac(f2s(d['diffval']),d['errjel'])
   alfa=d['alfa']
   d['krit']=[tcrit(1-alfa,df), tcrit(1-0.5*alfa,df)]



def perform():
   out=r'1-mintás t-próba\newline'+ujsor
   out+=r'\Mat{'+ujsor
   n=d['n']
   out+=r'n={n}'.format(n=n)+mujsor
   out+=g.atlag(sumjel=d['sumjel'], sumval=f2s(d['sumval']), n=n, res=f2s(d['meanval']))+mujsor
   out+=r's = '+d['sjel']+' = '+mujsor
   out+=r' = '+br(frac(f2s(d['sum2val']),str(n-1)))+r'^{\frac{1}{2}}'
   out+=r' = {s}'.format(s=f2s(d['sval']))+mujsor
   out+=r'\frac{{s}}{{\sqrt{n}}}'+' = '+frac(f2s(d['sval']), f2s(np.sqrt(n)))+' = '+f2s(d['errval'])+mujsor
   out+=r't = '+d['tjel']+' = '+f2s(d['tval'])+mujsor
   out+=d['krit'][0]+r'\hspace{1cm}'+d['krit'][1]
   print(out+'\n'+r'}'+ujsor)
