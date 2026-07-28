# -------------
# --- Tuple ---
# -------------

# Tuple with One Element

myTuple1 = ("Diaa",)
myTuple2 = "Diaa",

print(type(myTuple1))
print(type(myTuple2))

print(len(myTuple1))
print(len(myTuple2))

# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6)

c = a+b

d = a+("Diaa", True, -10.65)+b

print(c)
print(d)

# Tuple, List, String Repeat (*)

myString = "Diaa"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# Methods => count()

x = (1, 2, 3, 5, 5, 8, 1, 5, 9, 5, 6, 5)
print(x.count(5))

# Methods => index()

b = (1, 5, 2, 8, 6, 3, 7, 10.5, 9)
print(b.index(10.5))
print("The Position Of Index Is: {:d}".format(b.index(10.5)))
print(f"The Position Of Index Is: {b.index(10.5)}")

# Tuple Destruct

a = ("A", "B", 4, "Diaa", "C")

x, y, _, _, z = a

print(x)
print(y)
print(z)

# -----------------------------------------------------------------------------------
