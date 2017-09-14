def myDecorator(fn_name):
    def inner(name):
        st = fn_name(name) + ' How r u'
        return st
    return inner
    
@myDecorator
def fn(name):
    """ """
    return "Hi {}".format(name)
    
print fn('Ram')