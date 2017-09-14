def sample_decorator(func_name):
    def inner(name):
        name = func_name(name) + " How are you"
        return name
    return inner
    
@sample_decorator
def fn(name):
   """ """
   return "Hi {}".format(name)
   
print fn('Ram')