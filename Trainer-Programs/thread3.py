import time
import threading

def printer():
    for _ in range(3):
        time.sleep(1.0)
        print "hello"

thread = threading.Thread(target=printer)
thread.start()
thread.join()
print "goodbye"