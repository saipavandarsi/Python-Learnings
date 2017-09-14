def my_decorator(fn):
    def inner_fucntion(a, b):
        if a%2 == 0 and b%2 == 0:
            return fn(a, b)
        else:
            return 'both are not even'
    return inner_fucntion

@my_decorator
def sum(a, b):
    return a + b
    
print sum(2, 3)
#print sum(2, 4)