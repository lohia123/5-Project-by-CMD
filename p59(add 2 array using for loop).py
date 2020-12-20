from numpy import *
'''ary_1 = array ('i',[11,12,13])
ary_2 = array ('i',[14,15,16])
ary_3 = array ('i')
ary_len = len (ary_1) + len (ary_2)
for i in range (0,ary_len):
    ary_3.append (ary_1 [i])
    ary_3.append (ary_2 [i])
    if len (ary_3) == len (ary_1) + len (ary_2):
       print(ary_3)
       break'''

'''ary_1 = array ('i',[11,12,13])
ary_2 = array ('i',[14,15,16])
ary_1.extend(ary_2)
print(ary_1)'''

ary_1 = array([11,12,13])
ary_2 = array([14,15,16])
ary_3 = append(ary_1,ary_2)
print(ary_3)