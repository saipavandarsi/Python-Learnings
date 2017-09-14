"""
This module is giving Class example
"""
class A:
    """
       This module is giving Class example
    """
    a = 10
    b = 20

    def fn(self):
        """
           self is like this operator in java, but its needed if you give same variables
        """
        return "Hello"


z = A()
print dir(z)
print z.a
print z.b
print z.fn()
