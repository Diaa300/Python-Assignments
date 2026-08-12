# -----------------
# -- Loop => For --
# --  Training's --
# -----------------

# Range 


myRange = range(1, 101)

for number in myRange:

    print(number)

print('=' * 50) 

# Dictionary

mySkills = {

    "Html" : "50%",
    "Js" : "60%",
    "Css" : "70%",
    "PHP" : "80%",
    "Python" : "90%",
}

# print(mySkills["Css"])
# print(mySkills["Js"])

for skill in mySkills:

    # print(skill)

    print(f'My Progress in Language {skill} Is: {mySkills.get(skill)} ')