import xmltodict

import pdb;pdb.set_trace()

document_file = open("sample1.xml")
original_doc = document_file.read()
document_file.close()

document = xmltodict.parse(original_doc)

note = document['note']
print "Original XML file: {0}".format(original_doc)
print "Reminder for {0}, from {1}, content: {2}".format(note['to'], note['from'], note['body']) 
