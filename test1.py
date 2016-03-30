import os
import sys

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