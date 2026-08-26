# -----------------------
# -- Built In Function --
# -----------------------

# enumerate(iterable, start=0)

mySkills = ["HTML", "CSS", "PHP", "JS", "Python"]
mySkillCounter = enumerate(mySkills, 1)

for counetr, skill in mySkillCounter:

    print(f'{counetr} - {skill}')


print('=' * 50)

# help()

# print(help(print))

print('=' * 50)

# reversed()

mystring = 'Diaa'

print(reversed(mystring))

for letter in reversed(mystring):

    print(letter)


for s in reversed(mySkills):

    print(s)

print('=' * 50)