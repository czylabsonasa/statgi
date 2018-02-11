import sys

def olvas():
   d=dict()
   for line in sys.stdin:
      akt=line.split('=')
      if len(akt) != 2:
         continue
      if len(akt[0])==0 or len(akt[1])==0:
         sys.exit('hibas input')
      akt=[ s.strip() for s in akt ]
      #print(akt)
      d[akt[0]]=akt[1]

   for k in d:
      if k=='tipus' or k=='jelleg':
         continue
      #print(k, d[k])
      tmp=d[k].split(' ')
      tmp=[ float(s.strip()) for s in tmp ]
      if len(tmp)>1:
         d[k]=tmp
      else:
         d[k]=tmp[0]
      #print(k, d[k])
   return d


def f2s(x,d=2):
   return '%.{d}f'.format(d=d)%x



jellegT={'egyenlo':[ r' = ', r' \neq ' ], 'bal':[r' \ge ', r' < '], 'jobb':[r' \le ', ' > ']}

muhipT=r'H_0 : \mu{j0}{mu0}\\ H_1 : \mu{j1}{mu0}'

def muhip(j, mu0):
   return( muhipT.format(j0=j[0], j1=j[1], mu0=mu0) )

def sumjel(x1, xn):
   return( r'{x1}+\ldots +{xn}'.format(x1=f2s(x1), xn=f2s(xn)) )

def sum2jel(x1, xn, m):
   return( r'\left({x1}-{m}\right)^2+\ldots +\left({xn}-{m}\right)^2'.format(x1=f2s(x1), xn=f2s(xn), m=f2s(m) ) )


atlagT=r'\overline{{X}} = \frac{{{sumjel}}}{{{n}}} = \frac{{{sumval}}}{{{n}}} = {res}'

def atlag(sumjel, sumval, n, res):
   return( atlagT.format(sumjel=sumjel, sumval=sumval, n=n, res=res) )

ujsor='\n'
mujsor=r'\\[2ex]'+'\n'

def frac(a, b):
   return( r'\frac{{{a}}}{{{b}}}'.format(a=a, b=b))

def zjel(a):
   return( r'\left('+a+r'\right)')
