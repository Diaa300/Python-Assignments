# ---------------------------------------------------
# -- Function Packing Unpacking Arguments **KWArgs --
# ---------------------------------------------------

# def show_skills(*skills):

#     print(type(skills))

#     for skill in skills:

#         print(f'{skill}')

# show_skills("HTML", "CSS", 'JS')        

mySkills = {
    "HTML":"60%",
     "CSS":"70%",
     "JS ": "90%"
}

def show_skills(**skills):

    print(type(skills))

    for skill, value in skills.items():

        print(f'{skill} => {value}')

show_skills(HTML="60%", CSS="80%", JS = "90%")        
show_skills(**mySkills)        
