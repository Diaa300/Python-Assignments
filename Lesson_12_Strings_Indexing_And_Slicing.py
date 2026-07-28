"""
---------------
Strings Indexing & Slicing

 [1] All Data in Python is Object
 [2] Object Contain Elements
 [3] Every Element Has Its Own Index
 [4] Python Use Zero Based Indexing ( Index Start From Zero )
 [5] Use Square Brackets To Access Element
 [6] Enable Accessing Parts Of Strings, Tuples or Lists

 ---------------
 """

# Indexing ( Access Single Item )

mystring = "I Love Python" 
print (mystring[0]) #Index 0 => I 
print (mystring[4]) #Index 4 => v 
print (mystring[9]) #Index 9 => t

print (mystring[-1]) #Index -1 => Frist Character From End
print (mystring[-6]) #Index -6 => 6th Character From End

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print (mystring[8:11]) # yth
print (mystring[9:13]) # thon
print (mystring[:11]) # If Start Not Here Will Start From 0 (Zero) => (I Love Pyth)
print (mystring[3:]) # If End Not Here Will Go To The End => (ove Python)
print (mystring[:]) # Full Data 

print (mystring[::1]) # Full Data 
print (mystring[0::1]) # Full Data 
print (mystring[3::4])  
print (mystring[::])
print (type([1,2,3]))
print (type("Diaa"))