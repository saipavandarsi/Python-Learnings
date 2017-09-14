def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

print "1. add \n 2.sub \n 3.mul \n 4.div"
choice = int(input('select choice: ' ))

a = int(input('Enter first number:' ))
b = int(input('Enter second number:' ))

if choice == 1:
    print(a,"+",b,"=",add(a,b))
elif choice == 2:
    print sub(a,b)
elif choice == 3:
    print mul(a,b)
elif choice == 4:
    print div(a,b)
else:
    print "wrong inputs provided"



