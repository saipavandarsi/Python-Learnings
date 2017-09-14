import pickle

class A:
   a = 1
   b = 2
   
z = A()
fp = open('sample123.txt', 'w')
pickle.dump(z, fp)
fp.close()

fp = open('sample123.txt', 'r')
lst = pickle.load(fp)
fp.close()

print lst.a