import os
import sys

def fn(path, filename):
    a = os.path.join(path,filename)
    fp = open(a, 'r')
    content = fp.read()
    fp.close()
    return content

if __name__ == '__main__':
    path = sys.argv[0]
    filename = sys.argv[1]
    print fn(path,filename)
