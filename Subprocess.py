"""
This is a class to execute commands from command prompt
"""

import subprocess

#subprocess.call(['ls', '-la'], shell=True)

#PIPE is used to make the output as a tuple
p = subprocess.Popen(["python", "StringFormat.py"], stdout=subprocess.PIPE)

#p.communicate() is to print the object content
print p.communicate()
