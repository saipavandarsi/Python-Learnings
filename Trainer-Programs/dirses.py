import os

rootdir = 'C:\Users\Ramachandra\training'

for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        print os.path.join(dirpath, filename)