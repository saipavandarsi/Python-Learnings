import sys
import threading

class MyThread(threading.Thread):
    val = 1
    def run(self):
        if self.val:
            self._Thread__target(*self._Thread__args, **self._Thread__kwargs)
            print self._Thread__args
            print self._Thread__kargs

def func(a, b):
    print("a + b = %s" % (a+b))

thread = MyThread(target=func, args=(1,3))
thread.start()