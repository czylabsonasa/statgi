import gen as g
from gen import f2s, ujsor, mujsor

import numpy as np
from scipy.stats import norm


def zcrit(p):
   return( r'z_{{{a}}}={{{za}}}'.format(a=f2s(p,3), za=f2s(norm.ppf(p),3)))

d=dict()
def init(inp):
   global d
   d=inp
   if 'jelleg' in d:
      d['hip']=g.muhip(j=g.jellegT[d['jelleg']], mu0=d['mu0'])
   X=d['X']
   n=d['n']=len(X)
   d['sumval']=np.sum(X)
   d['sumjel']=g.sumjel(X[0], X[n-1])
   d['meanval']=np.mean(X)
   d['meanjel']=r'\frac{{{sumjel}}}{{{n}}}'.format(sumjel=d['sumjel'],n=n)
   d['diffval']=d['meanval']-d['mu0']
   d['diffjel']=r'{mean}-{mu0}'.format(mean=f2s(d['meanval']), mu0=f2s(d['mu0']))
   d['errval']=d['sigma']/np.sqrt(n)
   d['errjel']=f2s(d['errval'])
   d['zval']=d['diffval']/d['errval']
   d['zjel']=r'\frac{{{diffjel}}}{{{errjel}}}'.format(diffjel=d['diffjel'],errjel=d['errjel'])+'='+\
   r'\frac{{{diffval}}}{{{errjel}}}'.format(diffval=f2s(d['diffval']),errjel=d['errjel'])
   alfa=d['alfa']
   d['krit']=[zcrit(1-alfa), zcrit(1-0.5*alfa)]



def perform():
   out=r'1-mintás z-próba\newline'+ujsor
   out+=r'\Mat{'+ujsor
   #out+=d['hip']+mujsor
   out+=r'n={n}'.format(n=d['n'])+mujsor
   out+=g.atlag(sumjel=d['sumjel'], sumval=f2s(d['sumval']), n=d['n'], res=f2s(d['meanval']))+mujsor
   out+=r'z = '+d['zjel']+' = '+f2s(d['zval'])+mujsor
   out+=d['krit'][0]+r'\hspace{1cm}'+d['krit'][1]
   print(out+'\n'+r'}'+ujsor)
