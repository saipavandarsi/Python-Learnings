from sys import argv

print argv

def fn(a,b):
    return a+b

if len(argv) == 3:
    a = int (argv[1])
    b = int (argv[2])

    print "\n Result is....." + str(fn(a,b))

else:
    exit('\n USAGE : {} Needs 2 Parameters <<param1>> <<param2>>'.format(argv[0]))

