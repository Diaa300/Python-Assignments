# -------------------------
# ------ Set Methods ------
# -------------------------

#clear() 

a = {1, 2, 3, 4}
a.clear()
print(a)

# union()

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Diaa"}

print(b | c)
print(b.union(c, x))

# add()

d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)

# copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(5)

print(e)
print(f)

# remove()

z = {1, 2, 3, 4}
z.remove(1)
# z.remove(5)
print(z)

# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(5) 
print(h)

# pop()

i = {"Diaa", 1, 2, True, False, 1, 2, 3, 4, 5}
print(i.pop())

# update()

j = {1, 2, 3, 4}
k = {"Diaa", "Ragab", 1, 5, 6, 3, 2, 5}
j.update(["HTML", "CSS"])
j.update(k)
print(j)