"""
This module is giving Class example
"""
class A:
    """
       This module is giving Class example
    """
    a = 10
    b = 20

    def fn(self, c, d):
        """
           self is like this operator in java, but its needed if you give same variables
        """
        return c + d


z = A()
print dir(z)
print z.a
print z.b
print "\n"
print z.fn(10,200)
help(z.fn())

