# --------------------------------------
# -----Ternary Conditional Operator-----
# --------------------------------------

Country = "Egypt"

if Country == "Egypt" :
    print(f"The Weather in {Country} is 15")

elif Country == "KSA" :
     print(f"The Weather in {Country} is 30")

else :
     print("The Country is Not in The List")     


# Short If

movieRate = 18
age = 16

if age < movieRate :
     print("Movie S Not Good 4U") # Condition If True

else :
     print("Movie S Good 4U And Happy Watching") # Condition If False

print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")     

# Condition If True | If Condition | Else | Condition If False