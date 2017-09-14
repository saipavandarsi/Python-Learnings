a = 10

def func():
    a = 20
    return a

def global_var_use():
    global a
    a = a+1
    return a

print a


print func()
print global_var_use()