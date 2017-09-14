import time

from threading import Thread

def myfuntion(i):
    print "sleeping 5 secs from thread %d" % i
    time.sleep(5)
    print "\nfinished executing from Thread - %d" % i

for num in range(10):
    t = Thread(target=myfuntion, args=(num,))
    t.start()
