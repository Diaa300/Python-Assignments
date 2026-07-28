# Commissioning 01

print(type(100))
print(type(100.5))
print(type(100 + 5j))

print('=' * 50) # Separator

# Commissioning 02

my_complex = 1 + 2j
print(my_complex.real)
print(my_complex.imag)

print('=' * 50) # Separator

# Commissioning 03

num = 10
print(f"{num:.10f}")

print('=' * 50) # Separator

# Commissioning 04

num = 159.650
print(int(num))
print(type(int(num)))

print('=' * 50) # Separator

# Commissioning 05

print(100 - 115)  # -15
print(50 * 30)    # 1500
print(21 % 4)     # 1
print(110 // 11)  # 10
print(97 // 20)   # 4

print('=' * 50) # Separator

# Commissioning 06

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])
print(friends[-5])

print(friends[4])
print(friends[-1])

print('=' * 50) # Separator

# Commissioning 07

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[::2])
print(friends[1::2])

print('=' * 50) # Separator

# Commissioning 08

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[1:4])
print(friends[3:5])

print('=' * 50) # Separator

# Commissioning 09

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends[-2:] = ["Elzero", "Elzero"]
print(friends)

print('=' * 50) # Separator

# Commissioning 10

friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0, "Nasser")
print(friends)

friends.append("Salem")
print(friends)

print('=' * 50) # Separator

# Commissioning 11

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.remove("Osama")
friends.remove("Nasser")
print(friends)

friends.pop()
print(friends)

print('=' * 50) # Separator

# Commissioning 12

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends = friends + employees + school
print(friends)

print('=' * 50) # Separator

# Commissioning 13

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(sorted(friends))

friends.sort(reverse=True)
print(friends)

print('=' * 50) # Separator

# Commissioning 14

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(len(friends))

print('=' * 50) # Separator

# Commissioning 15

technologies = ["HTML", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])

print('=' * 50) # Separator

# Commissioning 16

myTuple = "Osama",

print(myTuple[0])
print(type(myTuple))

print('=' * 50) # Separator

# Commissioning 17

friends = ("Osama", "Ahmed", "Sayed")

friendslist = list(friends)
friendslist[0] = "Elzero"

friends = tuple(friendslist)

print(friends)
print(type(friends))

print(f"{len(friends)} Elements")

print('=' * 50) # Separator

# Commissioning 18

nums = (1, 2, 3)
letters = ("A", "B", "C")

nums_and_letters_one = nums + letters

print(nums_and_letters_one)
print(f"{len(nums_and_letters_one)} Elements")

print('=' * 50) # Separator

# Commissioning 19

my_tuple = (1, 2, 3, 4)

a, b, _, d = my_tuple

print(a)
print(b)
print(d)

print('=' * 50) # Separator
