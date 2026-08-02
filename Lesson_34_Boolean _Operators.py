# --------------------------
# -----Boolean Operators----
# --------------------------
# and
# or
# not
# --------------------------

age  = 16 
Country = "Egypt"
rank = 10

print("=" * 50)

print(age > 15 and Country == "Egypt" and rank > 0) # True
print(age > 15 and Country == "KSA" and rank > 0) # False

print("=" * 50)

# or

print(age > 40 or Country == "KSA" or rank > 20) # False
print(age > 40 or Country == "Egypt" or rank > 20) # True

print("=" * 50)

# not

print(not age < 20) # Not True = False 

print("=" * 50) 