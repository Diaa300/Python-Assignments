# ------------------------------------------------------
# --- Function Packing, Unpacking Arguments Training ---
# ------------------------------------------------------

mytuple = ("HTML", "CSS", 'JS')

myskills = {
    'GO' : '95%',
    'Python' : '75%',
    'MySQL' : '80%',
}

def show_skills(name, *skills, **skillwithprogress):

    print(f'Hello {name} \nSkills Without Progress Is: ')

    for skill in skills:

        print(f'- {skill}')

        print('Skill With Progress')

        for skill_key, skill_value in skillwithprogress.items():

            print(f'{skill_key} => {skill_value}')

show_skills('Diaa', *mytuple, **myskills)    