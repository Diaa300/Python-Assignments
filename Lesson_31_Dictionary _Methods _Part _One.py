# ------------------------------
# ----- Dictionary Methods -----
# ------------------------------

# clear()

user = {
    "Frist Name" : "Diaa",
    "Last Name" : "Ragab"
}

print(user)
user.clear()
print(user)

print('=' * 50) # Separator


# update()

member = {
    "name" : "Diaa"
}

print(member)
member["age"] = 16
print(member)
member.update({"country" : "Egypt"})
print(member)

print('=' * 50) # Separator

# copy()

main = {
    "Name" : "Diaa"
}

b = main.copy()
print(b)

main.update({"skills" : "eating"})
print(main)
print(b)

print('=' * 50) # Separator

# keys() + values()

print(main.keys())
print(main.values())

print('=' * 50) # Separator