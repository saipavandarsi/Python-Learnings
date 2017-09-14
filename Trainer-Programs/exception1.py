num = raw_input('please enter a number: ')
try:
   int(num)
except ValueError:
   print 'Cannot convert string to integer'
except IOError:
   print 'bla bla'
else:
   print "num : ", num
finally:
   print 'this executes always'   