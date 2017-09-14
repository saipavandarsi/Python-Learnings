num = raw_input('Please enter a number: ')

try:
    int(num)
    #print "num : ", num

except ValueError:
    print 'Can not convert String to integer or number'

except IOError:
    print 'IO Error Occured'

except:
    print 'Exception Occured'

# else is optional, we can write this code in try block itself.
else:
    print "num : ",num

finally:
    print 'Done Execution'
