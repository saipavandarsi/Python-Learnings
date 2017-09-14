a = 1

def fn():
   global a
   a = a + 1
   return a
   
print fn()