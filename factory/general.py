import zegy
import tegy
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
