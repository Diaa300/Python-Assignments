# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in

# String

name = "Diaa"

print("aa" in name)
print("a" in name)
print("i" in name)
print("D" in name)
print("d" in name)

print("#" * 50)

# List

friends = ["Diaa", "Ahmed", "Mohamed"]
print("Diaa" in friends)
print("Kadre" in friends)
print("Ahmed" in friends)
print("Mohamed" not in friends)

print("#" * 50)

# Using in And not in With Condition

countries_One = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
countrise_One_Discount = 80

countries_Two = ["Italy", "USA"]
countries_Two_Discount = 50

myCountry = "USA"

if myCountry in countries_One :
    print(f'Hello Because You From {myCountry} You Have A Discount Equal To ${countrise_One_Discount}')

elif myCountry in countries_Two :
    print(f"Hello Because You From {myCountry} You Have A Discount Equal To ${countries_Two_Discount}")
else :
    print("You Have No Discount")    