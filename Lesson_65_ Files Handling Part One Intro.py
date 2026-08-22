# --------------------
# --  File Handling --
# --------------------
# "a" Append Open File For Appending Values, Creat File If Not Exists
# "r" Read   [Deafault Value] Open File For Read And Give Error If File Is Not Exists
# "W" Write  OPen File For Writing, Creat File If Not Exists
# "x" creat  Creat File, Give Error If File Exists
#-------------------------------------------------------------

import os

# Main Current Working Directory
print(os.getcwd())

# Directory For the opened File
print(os.path.dirname(os.path.abspath(__file__))) 

# Change Currnet Working Directory 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

# print(os.path.abspath(__file__))  

file = open("diaa.txt") 

 

