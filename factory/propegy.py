import gen as g
from gen import f2s, ujsor, mujsor, frac, br, cbr

import numpy as np
from scipy.stats import norm

def zcrit(p):
   return( r'z_{{{a}}}={{{za}}}'.format(a=f2s(p,3), za=f2s(norm.ppf(p),3)))

d=dict()
def init(inp):
   global d
   d=inp
   n=d['n']
   k=d['k']
   p0=d['p0']
   phat=k/n
   alfa=d['alfa']
   d['diffval']=phat-p0
   d['diffjel']=f2s(phat)+'-'+f2s(p0)
   d['errval']=np.sqrt(p0*(1-p0)/n)
   s=f2s(p0)+br('1-'+f2s(p0))
   sval=p0*(1-p0)
   d['errjel1']=br(frac(s, str(n)))+r'^\frac{1}{2}'
   d['errjel2']=br(frac(f2s(sval), str(n)))+r'^\frac{1}{2}'
   d['zval']=d['diffval']/d['errval']
   d['zjel']=frac(d['diffjel'],f2s(d['errval']))
   d['thrval']=n*min(p0,1-p0)
   d['thrjel']=str(n)+r'\min('+f2s(p0)+','+f2s(1-p0)+r')'
   d['krit']=[zcrit(1-alfa), zcrit(1-0.5*alfa), \
   zcrit(alfa), zcrit(0.5*alfa)]



def perform():
   out=r'1-mintás arány-próba\newline'+ujsor
   out+=r'\Mat{'+ujsor
   n=d['n']
   out+=d['errjel1']+' = '+d['errjel2']+' = '+f2s(d['errval'])+mujsor
   out+=r'z='+frac(d['diffjel'],f2s(d['errval']))+'='\
   +frac(f2s(d['diffval']), f2s(d['errval']))+' = '+f2s(d['zval'],4)+mujsor
   out+=r'\text{küszöb}='+d['thrjel']+' = '+f2s(d['thrval'])+mujsor
   out+=d['krit'][0]+r'\hspace{1cm}'+d['krit'][1]+mujsor
   out+=d['krit'][2]+r'\hspace{1cm}'+d['krit'][3]
   print(out+'\n'+r'}'+ujsor)
