# -------------------------
# ------ Set Methods ------
# -------------------------

# difference()

a = {1, 2, 3, 4, 5}
b = {1, 2, "Diaa", "Mohamed"}
print(a)
print(a.difference(b)) # a-b
print(a)

print('=' * 40) # Separator

# difference_update()

c = {1, 2, 3, 4, 5}
d = {1, 2, "Diaa", "Mohamed"}
print(c)
c.difference_update(d) # c - d
print(c)

print('=' * 40) # Separator

# intersection()

e = {1, 2, 3, 4, 5, "X", "Diaa"}
f = {"Diaa", "X", 2}
print(e)
print(e.intersection(f)) # e & f
print(e)

print('=' * 40) # Separator

# intersection_update()

g = {1, 2, 3, 4, 5, "X", "Diaa"}
h = {"Diaa", "X", 2}
print(g)
g.intersection_update(h) # g & h
print(g)

print('=' * 40) # Separator

# symmetric_difference()

i = {1, 2, 3, 4, 5, "X"}
j = (1, 2, "X")
print(i)
print(i.symmetric_difference(j)) # i ^ j
print(i)

print('=' * 40) # Separator

# symmetric_difference_update()

k = {1, 2, 3, "Diaa", 5}
l = {1, 2, 3, "Ahmed", 5}
k.symmetric_difference_update(l)
print(k)

print('=' * 40) # Separator
