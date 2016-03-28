import os
import sys

print('As usual printing Hello World!')
print(os.getcwd())
print(sys.builtin_module_names)
print(dir())
print(dir(__builtins__))

#giving argument in the terminal
ar=sys.argv
print("This is argument 1: "+ar[1])