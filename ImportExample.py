
"""
USE OF IMPORT:
    import <<Filename>> imports all the variable and methods
    if you want to protect you need to write code in this block (if __name__ == '__main__':)
    calling this /Usage of this import is
        Goto Python Prompt
        import ImportExample
        ImportExample.fn(10,20)

Use Of FROM:
    >> from ImportExample import fn
    >>fn(20,30)
    This imports fn Function FROM ImportExample

"""

from sys import argv

def fn(a,b):
    return a+b

if __name__ == '__main__':
    fn(2,3)

    if len(argv) == 3:
        a = int (argv[1])
        b = int (argv[2])

        print "\n Result is....." + str(fn(a,b))

    else:
        exit('\n USAGE : {} Needs 2 Parameters <<param1>> <<param2>>'.format(argv[0]))

