"""
This mpdinadasdas
"""

from sys import argv, exit

def fn(a, b):
     """
     this function takes params/a/b
     retsdsdasdsa
     """
     return a+b
     
if __name__ == '__main__':
   if len(argv) > 2:
       a = argv[1]
       b = argv[2]
       print fn(a, b)
   else:
       exit("Usage: python {} <<params/a/b>>".format(argv[0]))  