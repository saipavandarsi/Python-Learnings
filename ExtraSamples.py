#creating map as input, and getting result in map
#we have map functions
def fn(i):
   return i*2

print map(fn, [1,2,6,7])


#filter is used for filtering the sequence and gives the result in sequence
def fn(n):
    return n%2 == 0

print filter(fn, [1,2,3,4,7,18,100,4,5,90])
print map(fn, [1,2,3,4,7,18,100,4,5,90])


#Reduce will gives a result from the map / sequence
def fn(x, y):
    return x+y

print reduce(fn, [1,2,3,4,5])
print reduce(fn, [1,2,3,4])

#Lambda functions -- 1 line runtime functions
a = (lambda x, y: x+y)(20,30)
print 'Lambda Result is........  ' + str(a)


#Range is Iterator Object , if we put YIELD then iterator object
# Converts to Generator Object.
def iterator_object(n):
    for i in range(n):
        print i,

def convert_iterator_to_generator(n):
    for i in range(n):
        yield i,


iterator_object(5)
a = convert_iterator_to_generator(10)








