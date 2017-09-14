import time

from threading import Thread

def myfuntion(i):
    print "sleeping 5 secs from thread %d" % i
    time.sleep(1)
    print "finished Thread - %d" % i

for num in range(10):
    t = Thread(target=myfuntion, args=(num,))
    t.start()
    t.join()