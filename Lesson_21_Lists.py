# --------------------------------
# --Lists--
# --------- 
# [1] Lists Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index TO Access Item
# [3] List Are Mutable => Add, Delete, Edit 
# [4] List Items Is Not Unique 
# [5] List Can Have Different Data Types 

# ----------------------------------

myAwesome = ["One", "TWo", "One", 1,"Diaa", 11.56, False]
print (myAwesome) # whole List
print (myAwesome[4]) # Diaa
print (myAwesome[0]) # One
print (myAwesome[-1]) # False
print (myAwesome[3]) # 1
print (myAwesome[-2]) # 11.56
print (myAwesome[-3]) # Diaa

print (myAwesome[-3:]) # ['Diaa', 11.56, False]
print (myAwesome[::2]) # ['One', 'One', 'Diaa', False]

print (myAwesome) # whole List

myAwesome[-2] = 16.84
print (myAwesome) 
myAwesome[:] = [3]
print (myAwesome)