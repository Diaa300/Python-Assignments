# --------------------
# -- String Methods --
# --------------------

# replace(Old Value, New Value, Count)

a = "Hello Ahmed Hi Ahmed"
print (a.replace("Ahmed","Diaa"))
print (a.replace("Ahmed","Diaa", 1))
print (a.replace("Ahmed","Diaa", 2))

# join(iterable)

My_list = ["Diaa", "Ragab", "ElSayed"]
print ("-".join(My_list))
print (" ".join(My_list))
print (", ".join(My_list))
print (type(", ".join(My_list)))