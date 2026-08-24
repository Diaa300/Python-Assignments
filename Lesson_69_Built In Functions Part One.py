# ------------------------
# -- Built In Functions --
# ------------------------
# all()
# any()
# bin()
# id()
# ------------------------

x = [1, 2, 3, 4, []]

if all(x):

    print("All Elements Is True")

else:

    print("Theres At Least One Element Is False")


x = [1, 2, 3, 4]

if any(x):

    print("Theres At Least One Element Is True")

else:

    print("Theres No Any True Element")



print(bin(100))





a = 1
b = 2

print(id(a))
print(id(b))


