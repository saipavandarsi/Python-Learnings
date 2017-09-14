import json

import pdb;pdb.set_trace()

#open() is used to read a file -- in Read mode and read()

json_string = open("jsonSample.json").read()

#Converting str Object to python Object
parsed_json = json.loads(json_string)

#Parsing Data
output = parsed_json

print output
