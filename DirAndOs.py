import os

#rootdir = ''

#dirpath gives the directory
#dirname gives all directories inside the directory
#filename gives all the filenames inside the directory
for dirpath, dirnames, filenames in os.walk("."):
    #print dirpath
    #print dirnames
    #print filenames

    for filename in filenames:
        print os.path.join(dirpath, filename)
