def fn(st):
    """ """
    fp = open('testfile.txt', 'r')
    lines = fp.readlines()
    fp.close()
    
    line_no, position = 0, 0
    
    for line in lines:
        if st in line:
            line_no = line_no + 1
            position = line.index(st)
            print line_no, position
    if not line_no:
        print "{} not found in file".format(st)
    
fn('Ram')
fn('Raju')
            
    