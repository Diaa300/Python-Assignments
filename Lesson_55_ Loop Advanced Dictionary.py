# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------

mySkill = {
    "Html" : "90%",
    "Css" :"80%",
    "JS" : "70%",
    "PHP" : "60%"
}

# print(mySkill.items())

# for skill in mySkill:

#     print(f"{skill} => {mySkill[skill]}")

for skill_key, skill_progress in mySkill.items():

    print(f"{skill_key} => {skill_progress}")
    
myUltimateSkills = {
    "HTML" :{
        "Main" : "80%",
        "Pugjs" : "80%"
    },
    "CSS" : {
        "Main" : "90%",
        "Sass" : "70%"
    }
}

for main_key, main_value in myUltimateSkills.items():

    print(f"{main_key} Progress Is: ")

    for skill_key, skill_value in main_value.items():

        print(f'- {skill_key} => {skill_value}')

