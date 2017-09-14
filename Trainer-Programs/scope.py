a = 1

def test():
     a = 5
     a = a + 1
     return a
	 
def t():
     a = test()
     print a
	 
test()
t()