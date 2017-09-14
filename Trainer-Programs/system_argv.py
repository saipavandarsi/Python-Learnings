import sys

def fn(a, b):
    return a + b

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        sys.exit('Usage: %s Should provive two arguments' % sys.argv[0])
        
    print fn(sys.argv[1], sys.argv[2])