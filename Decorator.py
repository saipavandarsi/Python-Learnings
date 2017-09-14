"""
Decorator1 and decorator2 methods
"""
def sample_decorator(func_name):
    def inner(name):
        name = func_name(name) + "\t How Are You Doing.....??"
        return name
    return inner

def sample_decorator2(func_name):
    def wrapper(name):
        name = func_name(name) + "\t Had Lunch???"
        return name
    return wrapper

#sample_decorator is decorator, display is a funtion uses decorator
# Here, display in func_name. name is parameter for inner method
#multi level decorator --
# The order of execution: bottom --> top
@sample_decorator2
@sample_decorator
def display(name):
    return "Hi {}".format(name)

# calling method
print display('Shruthi')