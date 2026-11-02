# ---------------------------
# --- Iterable Vs Iterator --
# ---------------------------

mystrig = "Diaa"

mylist = [1, 2, 3, 4, 5]

for letter in mystrig:

    print(letter, end="_")

for numbers in mylist:

    print(numbers, end="*")


myItrerator = iter(mystrig)

print(next(myItrerator))
print(next(myItrerator))
print(next(myItrerator))
print(next(myItrerator))
# print(next(myItrerator))

for letter in iter("Diaa"):

    print(letter, end= " ""\n")

print("#" * 50)

# ------------------------------
# Assignment 1 - Iterable
# ------------------------------

mystring = "Diaa"
dlist = [1, 2, 3, 4, 5]
mytuple = ("Red", "orange", "Yellow")

for mmm in mystring:

    print(mmm, end="_")

for nnn in dlist:

    print(nnn)

for bbb in mytuple:

    print(bbb)

print("#" * 50)

# ------------------------------
# Assignment 2 - Iterator
# ------------------------------

ls = ["Diaa", "Kadre", "Ahmed", "Eyad"]

myiter = iter(ls)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# print(next(myiter))

print("#" * 50)

# ------------------------------
# Assignment 3 - Function
# ------------------------------

lt = ["elzero", "osama", "Diaa", "Eyad" ]

def show_items(my_list):

    if not isinstance(my_list, list):

        raise TypeError("Input must be a list")
    
    if len(my_list) < 2:

        print("Not Enough")
    else:
    
        my_iter = iter(my_list)

        print(next(my_iter))
        print(next(my_iter))



show_items(lt)

print("#" * 50)