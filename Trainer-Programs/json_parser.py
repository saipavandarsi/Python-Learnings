import json

# reading json content from file system
json_string = open('sample.json').read()
import pdb;pdb.set_trace()
# converting str object to python object
parsed_json = json.loads(json_string)

# parsing data
output = parsed_json['two']['list'][0]['item']

# printing output
print output