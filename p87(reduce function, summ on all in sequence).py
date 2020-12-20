list1 = [78,12,53,58,47,99,14,26,23,31,41,79]
from functools import reduce
# sum=reduce((lambda x,y:x+y),list1)
# print(sum)
Max=reduce((lambda x,y:x if x<y else y),list1)
print(Max)