class A:
   a = 1
   b = 2
   
obj = A()

import pickle

#fp = open('output1.txt', 'w')
#pickle.dump(obj, fp)
#fp.close()

fp = open('output1.txt', 'r')
obj = pickle.load(fp)
fp.close()


print obj.a

