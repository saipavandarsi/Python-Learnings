def table(n):
     for i in range(1,11):
          print "{} * {} = {}".format(n, i, n*i)
        
n = raw_input('please enter number here: ')		
table(int(n))