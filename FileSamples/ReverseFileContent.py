#File content Reversing

#Using read()
file = open('myfile.txt', 'r')
content = file.read()
print content
print content[::-1]

# Using ReadLines
file = open('myfile.txt', 'r')
content_lines = file.readlines()
#content_lines[::-1] is to reverse lines
for line in content_lines[::-1]:
    #print characters in reverse
    print line[::-1] ,





