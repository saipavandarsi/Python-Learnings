"""
Encapsulation is acheived using private Variables/Methods.
"""
class Demo:
    __a = 1
    b = 2

    def fn(self):
        return 'Hello...' + str(self.__a)

    def __gn(self):
        return "Welcome, this is private Method"


z = Demo()
print str(z.b) + "\n"
print z.fn()


