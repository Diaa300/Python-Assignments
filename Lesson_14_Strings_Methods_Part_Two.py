# --------------------
# -- String Methods --
# --------------------

# split() rsplit()

a = "I Love Python And PHP"
print (a.split())

a = "I-Love-Python-And-PHP"
print (a.split("-"))

a = "I-Love-Python-And-PHP"
print (a.split("-",2))

a = "I-Love-Python-And-PHP"
print (a.split("-",3))

d = "I-Love-Football-And-Swiming"
print (d.rsplit("-",3))

# center()

e = "Diaa Ragab"
print (e.center(20)) # Spaces
print (e.center(20, "#")) # Hashes

# count()

f = "I Love Python And PHP Beacause PHP Is Easy"
print (f.count("PHP"))
print (f.count("PHP", 5, 21))

# swapcase()

g = "I LOVE PYTHON"
h = "i love python"
print (g.swapcase())
print (h.swapcase())

# startwith()

d = "I Love Python And PHP Beacause PHP Is Easy"
print (d.startswith("I"))
print (d.startswith("s",28,))

# endswith()

J = "I Love Python And PHP Beacause PHP Is Easy"
print (J.endswith("y"))
print (J.endswith("e",0 ,6))