import zegy, tegy, chi2sigma, propegy
from gen import olvas

inp=olvas()
#print(inp)
while 1==1:
   if inp['tipus']=='zegy':
      zegy.init(inp)
      zegy.perform()
      break
   if inp['tipus']=='tegy':
      tegy.init(inp)
      tegy.perform()
      break
   if inp['tipus']=='chi2sigma':
      chi2sigma.init(inp)
      chi2sigma.perform()
      break
   if inp['tipus']=='propegy':
      propegy.init(inp)
      propegy.perform()
      break


