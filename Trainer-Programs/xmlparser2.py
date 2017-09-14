import xml.etree.ElementTree as ET

with open('sample2.xml', 'r') as f:
    input = f.read()

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print 'User count:', len(lst)

for item in lst:
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get("x")