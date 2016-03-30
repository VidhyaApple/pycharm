import os
import sys
from os.path import exists
'''
print('As usual printing Hello World!')
print(os.getcwd())
print(sys.builtin_module_names)
print(dir())
print(dir(__builtins__))

#giving argument in the terminal
ar1=sys.argv
print("This is argument 1: "+ar1[1])
print("This is argument 2: "+ar1[2])
print("This is argument 3: "+ar1[3])

print("Enter name:")
print("Hi "+input('> ')+" welcome!")
'''

#create copy function as terminal command line
copyinfo=sys.argv
if copyinfo[1] == "copy":
    if exists(copyinfo[2]):
        with open(copyinfo[2]) as copyfile:
            copyfile_content=copyfile.read()
        tocopyfile=open(copyinfo[3],"w")
        print(copyfile_content,file=tocopyfile)
        tocopyfile.close()
    else:
        print("No file exists to copy!")

