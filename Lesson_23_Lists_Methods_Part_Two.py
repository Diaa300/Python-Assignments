# ---------------------------------
# ----------Lists Methods----------
# ---------------------------------

# clear()

a = [1, 2, 3, 4, 5]
a.clear()
print(a)

# copy()

b = [1, 2, 3, 4, 5]
c = b.copy()

print(b) # Main List
print(c) # Copied List

b.append(6)

print(b) # Main List
print(c) # Copied List

# count()

d = [1, 2, 6, 1, 100, 6, 3, 1, 5, 1, 8, 1]
print(d.count(1))

# index()

e = ["Mohamed", "Ahmed", "Diaa", "Osama"]
print(e.index("Diaa"))

# insert()

y = [1, 2, 3, 4, "A", "B"]

y.insert(0, "Test")
y.insert(-6, "Diaa")
y.insert(-1, "A&B")

print(y)

# pop()

z = [1, 2, 3, 4, "A", "B"]
print(z.pop(3))
print(z.pop(2))
print(z.pop(-1))
