# ------------------------------
# ----- Dictionary Methods -----
# ------------------------------

# setdefault()

user = {
    "Name" : "Diaa"
}

print(user)
print(user.setdefault("Name" , "Osama"))
print(user)

print(user.setdefault("Age" , 16))
print(user)

print('=' * 50) # Separator

# popitem()

member = {
    "name" : "Diaa",
    "skill" : "Sleeping"
}

member.update({"age" : 16})

print(member.popitem())

print('=' * 50) # Separator

# items()

player = {
    "name": "Cristiano Ronaldo",
    "skill": "Rainbow Flick"
}

allItems = player.items()
print(player)

player["rating"] = 99
print(allItems)

print('=' * 50) # Separator

# fromkeys()

a = ("MyKeyOne", "MyKeyTwo", "MyKeyThree")
b = "X"

print(dict.fromkeys(a , b))

print('=' * 50) # Separator
