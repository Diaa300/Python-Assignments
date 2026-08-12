# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

# people = ["Diaa", "Mohamed", "Kadre", "Ahmed"]

# skills = ["Html", "Css", "Js"]

# for person in people: # Outer Loop 
    
#     print(f"{person} Skills's : ")

#     for skill in skills: # Inner Loop

#         print(f"- {skill}")


peoples = {
    "Diaa":{
        "Python" :"90%",
        "Html" : "60%",
        "Css" : "80%"
    },
    "Mohamed" : {
        "PHP" : "90%",
        "JS" : "80%",
        "C++" : "95%"
    },
    "Kadre" : {
        "C#" : "80%",
        "Java" : "70%",
        "Swift" : "90%"
    }
}


# print(peoples["Diaa"])
# print(peoples["Kadre"]["C#"])

for name in peoples:
    
    print(f"Skills And Progress For {name} Is :")

    for skill in peoples[name]:

        print(skill)