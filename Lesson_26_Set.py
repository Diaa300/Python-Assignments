# -----------------
# ------ Set ------
# -----------------
# [1] Set Items Are Enclosed In Curly Braces 
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done 
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Are Unique
# ----------------------------------------------

# Not Ordered And Not Indexed

mySetOne = {"Diaa", "Mohamed", 100}
print(mySetOne)
# print(mySetOne[0])

# Slicing Cant Be Done 

mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:4])

# Has Only Immutable Data Types

# mySetThree = {1, 2, 3, "Diaa", True, 10.5, [8, 9, 10]} # unhashable type: 'list'
mySetThree = {1, 2, 3, "Diaa", True, 10.5, (8, 9, 10)}
print(mySetThree)

# Items Are Unique

mySetFour = {1, 2, 3, "Diaa", "One", "Ahmed", "Diaa", 4, 1, 3, 5, 9}
print(mySetFour)