# ---------------------------------
# ----------Lists Methods----------
# ---------------------------------

# append()

myfriends = ["Mohmed", "Mahmoud", "Ahmed"] 
myoldfriends = ["Sayed", "Saeed"]
myfriends.append("Kadre")
myfriends.append(15.52)
myfriends.append(120)
myfriends.append(myoldfriends)

print(myoldfriends[1]) # Saeed
print(myfriends) # ['Mohmed', 'Mahmoud', 'Ahmed', 'Kadre', 15.52, 120, ['Sayed', 'Saeed']]
print(myfriends[0:2]) # ['Mohmed', 'Mahmoud']
print(myfriends[0]) # Mohmed
print(myfriends[2]) # Ahmed

# _________________________________________________________________________________________________________________

# extend()

a = [1, 2, 3, 4]
b= ["A, B, C, D"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# _________________________________________________________________________________________________________________

# remove()

x = [1, 2, 3, 4, "Diaa", "Osama", True, "Diaa", "Osama", "Diaa"]

x.remove("Osama")
print(x)
x.remove("Diaa")
print(x)

# _________________________________________________________________________________________________________________

# sort()

y = [36, 58, -9, -82, 17, 54, -34]

y = ["A", "Z", "C"]
y.sort(reverse=True)
print(y)
y.sort(reverse=False)
print(y)
# y.sort()
print(y)
y.sort(reverse=False)
print(y)
y.sort(reverse=True)
print(y)

# _________________________________________________________________________________________________________________

# reverse()

z = [10, 80, 84, 94, "Diaa", -60, 159.57]

z.reverse()
print(z)