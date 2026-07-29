# التكليف 01

my_list = [1, 2, 3, 3, 4, 5, 1]

unique_list = list(set(my_list))

print(*unique_list, sep=", ")

print(type(unique_list))

unique_list.pop()
print(*unique_list, sep=", ")

print('=' * 50) # Separator

# التكليف 02

nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums | letters)
print(nums.union(nums, letters))
nums.update(letters)
print(nums)

print('=' * 50) # Separator

# التكليف 03

my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set)

my_set.update(["A", "B"])
print(my_set)

print('=' * 50) # Separator

# التكليف 04

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

print('=' * 50) # Separator

# التكليف 05

skills = {
    "HTML": "90%",
    "CSS": "80%",
    "Python": "30%"
}

print(f'"HTML Progress Is {skills["HTML"]}"')
print(f'"CSS Progress Is {skills["CSS"]}"')
print(f'"Python Progress Is {skills["Python"]}"')

skills["AI"] = "20%"

print(f'"AI Progress Is {skills["AI"]}"')

print('=' * 50) # Separator