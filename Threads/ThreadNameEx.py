import threading
import time

def worker():
    print threading.currentThread().getName(), 'starting....'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting...'

def my_service():
    print threading.currentThread().getName(), 'starting....'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting...'


t = threading.Thread(name='myserviceThread', target=my_service)
w = threading.Thread(name='workerThread', target=worker)
w2 = threading.Thread(target=worker)
#t2 = threading.Thread(target=my_service)

w.start()
t.start()
#t2.start()
w2.start()
w2.join()
