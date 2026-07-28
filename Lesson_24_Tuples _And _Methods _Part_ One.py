# ---------------------------
# --- Tuple ---
# -------------
# [1] Tuple Items Are Enclosed in Parentheses => ()
# [2] You Can Remove The Parentheses If You Want  
# [3] Tuple Are Ordered, To Use Index to Access Item 
# [4] Tuple Are Immutable => You Cant Added Or Delete 
# [5] Tuple Items Is Not Unique
# [6] You Can Have Different Data Types 
# [7] Operators Used in Strings and Lists Available In Tuples
# ---------------------------

# Tuple syntax & Tuple Test

MyAwesomeTupleOne = ("Diaa", "Ahmed")
MyAwesomeTupleTwo = "Diaa","Ahmed"

print(MyAwesomeTupleOne)
print(MyAwesomeTupleTwo)

# Tuple Indexing

MyAwesomeTupleThree = (1, 2, 3, 4, 5, 6, 7)
print(MyAwesomeTupleThree[0])
print(MyAwesomeTupleThree[-1])
print(MyAwesomeTupleThree[3])
print(MyAwesomeTupleThree[-2])

# Tuple Assign Values

MyAwesomeTupleFour = (1, 2, 3, 4, 5, 6, 7)
# MyAwesomeTupleFour[3] = "Three"
# MyAwesomeTupleFour[3] = []
# print(MyAwesomeTupleFour) # 'tuple' object does not support item assignment

# Tuple Items

MyAwesomeTupleFive = ("Diaa", "Diaa", "Three", 1, 2, 3, 100.5, True)

print(MyAwesomeTupleFive[1])
print(MyAwesomeTupleFive[-2])
print(MyAwesomeTupleFive[-1])

