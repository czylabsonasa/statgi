jellegT={'egyenlo':[ r' = ', r' \neq ' ], 'bal':[r' \ge ', r' < '], 'jobb':[r' \le ', ' > ']}

muhipT=r'''
H_0 : \mu{j0}{mu0}\\
H_1 : \mu{j1}{mu0}\\
'''

def muhip(j, mu0):
   return( muhipT.format(j0=j[0], j1=j[1], mu0=mu0) )

def sumjel(x1, xn):
   return( r'{x1}+\ldots +{xn}'.format(x1=x1, xn=xn) )

atlagT=r'''
\overline{{x}} = \frac{{{sumjel}}}{{{n}}} = \frac{{{sumval}}}{{{n}}} = {res}
'''

def atlag(sj, sv, n, r):
   return( atlagT.format(sumjel=sj, sumval=sv, n=n, res=r) )
