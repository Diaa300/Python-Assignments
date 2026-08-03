# -------------------
# ---- User Input----
# -------------------

fName = input("What's Your Frist Name ? ")
mName = input('What\'s Your Middle Name ? ')
lName = input("What's Your Last Name ? ")

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName} {lName} Happy To See You.")