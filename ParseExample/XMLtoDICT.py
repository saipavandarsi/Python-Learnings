import xmltodict

import pdb;pdb.set_trace()

#open() is used to read a file -- in Read mode
document_file = open("Version.xml")

original_doc = str(document_file.read())
print original_doc
document_file.close()

document = xmltodict.parse(original_doc)

hibernatemapping = document['hibernate-mapping']

print "Original XML file: {0}".format(original_doc)
print "Reminder for {0}".format(str(hibernatemapping['class']))

