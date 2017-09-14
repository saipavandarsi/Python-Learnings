class A:
    a = 1111
    b = 2222
    def fn(self):
        print self.a + self.b


class B:
    c = 3333

class C(A,B):
    d = 4444


_bobj = B()
print _bobj.c

_cobj = C()
print _cobj.a , _cobj.b, _cobj.c, _cobj.d
print _cobj.fn()
