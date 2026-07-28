# --------------------
# -- String Methods --
# --------------------

# index(Substring, Start, End)

a = "I Love Python"
print (a.index("P")) #Index Number 7
print (a.index("P",0 ,10)) #Index Number 7
# print (a.index("P",0 ,5)) # Through Error 

# find(Substring, Start, End)

b = "I Love Python"
print (b.find("P")) # Index Number 7
print (b.find("P",0 ,10)) # Index Number 7
print (b.find("P",0 ,5)) # -1

# rjust(Width, Fill char) ljust(Width, Fill char)

c = "Diaa"
print (c.rjust(8))
print (c.rjust(8, "@"))

d = "Diaa"
print (d.ljust(12))
print (d.ljust(12, "#"))

# splitlines()

e = """ Frist Line 
Second Line
Third Line""" 
print (e.splitlines()) 

f = "Frist Line\nSecond Line\n Third Line" 
print (f.splitlines()) 

# expandtabs()

g = "Hello\tWorld\tI\tLove\tPython"
print (g.expandtabs(2))

one = "I Love Python And 3G"
print(one.istitle())
two = "I Love Python And 3g"
print(two.istitle())

three = "  "
print (three.isspace())

four = "I Love Python"
print (four.islower())
five = "i love python"
print (five.islower())

six = "Diaa_Ragab"
seven = "DiaaRagab100"
eight = "Diaa--Ragab"

print(six.isidentifier())
print(seven.isidentifier())
print(eight.isidentifier())

x = "AaaaaaBbbbbb"
y = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
print (x.isalpha())
print (y.isalpha())

u = "AaaaaaBbbbbb"
z = "AaaaaaaaaBbbbbbbbbbbbbFfffffff12121212"
print (u.isalnum())
print (z.isalnum())
