# --------------------
# -- String Methods --
# --------------------

# strip() rstrip() lstrip ()
a = "I Love Python"
b = "     My Name Is Diaa      "
print (len(a))
print (len(b))

x = "     Hello World       "
print (x.strip())
print (x.rstrip())
print (x.lstrip())


x = "#@#@#@#@#Hello World#@#@##@##"
print (x.strip("#@"))
print (x.rstrip("#@"))
print (x.lstrip("#@"))

# title()

b = "I Love 2d Graphics and 3g Technology and Python"
print (b.title())


# capitalize()

b = "I Love 2d Graphics and 3g Technology and Python"
print (b.capitalize())

# zfill()

c, d, e, f = "1", "11", "111", "1111"
print (c.zfill(4))
print (d.zfill(4))
print (e.zfill(4))
print (f.zfill(4))

# upper()

g = "diaA RaGAp"
print (g.upper())

# lower()

h = "DIaA rAGap"
print (h.lower())
