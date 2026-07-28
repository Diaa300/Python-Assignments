# -------------------------
# ------ Set Methods ------
# -------------------------

# issuperset()

a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b)) # True
print(a.issuperset(c)) # False

print('=' * 50) # Separator

# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3,}
f = {1, 2, 3, 4, 5}
print(d.issubset(e)) # False
print(d.issubset(f)) # True

print('=' * 50) # Separator

# isdisjoint()

g = {1, 2, 3, 4, 5}
h = {6, 7, 8, 9, 10.5}
i = {1, 2, 3, 4}
print(g.isdisjoint(h)) # True
print(g.isdisjoint(i)) # False