#!/usr/bin/env python3

#version control min python3

import sys
if sys.version_info[0] < 3:
	raise Exception("You need Python3 or newer, try installing it or"\
    " running the script as python3")
  
from programFiles.mainmenu import mainmenu


print('#######################')
print('#                     #')
print('# Welcome to CubiX DB #')
print('#                     #')
print('#######################')

mainmenu()
#when we exit
print('Bye!')

