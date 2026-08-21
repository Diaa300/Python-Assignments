# ==================== Assignment 01 ====================

def calculate(n1, n2, op_type = "add"):

    op = op_type.strip().lower() 

    if op == "add" or op == "a":

        return n1 + n2

    elif op == "subtract" or op == "s":

        return n1 - n2

    elif op == "multiply" or op == "m":

         return n1 * n2 

    else:
        return "Operation Not Found"


print(calculate(10, 20))             # 30
print(calculate(10, 20, "Add"))      # 30
print(calculate(10, 20, "a"))        # 30
print(calculate(10, 20, "A"))        # 30

print(calculate(10, 20, "S"))        # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m"))        # 200

print('=' * 50)

# ==================== Assignment 02 ====================

def addition(*numbers):

    result = 0

    for num in numbers:

        if num == 10:

            continue

        elif num == 5:

            result -= 5

        else:

            result += num

    return result


print(addition(10, 20, 30, 10, 15))          # 65
print(addition(10, 20, 30, 10, 15, 5, 100))  # 160

print('=' * 50)

# ==================== Assignment 03 ====================

def show_skills(name, *skills):

    if skills:

        print(f'Hello {name} Your Skills Are: ')

        for skill in skills:

            

            print(f'- {skill}')

    else:

        print(f"Hello {name} You Have No Skills To Show")    


show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")

print('=' * 50)

# ==================== Assignment 04 ====================

def say_hello(name = "Unkown", age = "Unkown", country = "Unkown" ):

    print(f"Hello Your Name Is {name} Your Age Is {age} And You Live In {country}")

say_hello("Diaa", 16, "Egypt")   
say_hello()

print('=' * 50)

# ==================== Assignment 05 ====================

def get_score(**score):

    for score_key, score_value in score.items():

        print(f'{score_key} => {score_value}')

get_score(Math = 90, Scince = 80, Language = 70)

print("=" * 50)

# ==================== Assignment 06 ====================

def get_people_scores(name = "", **skills): 

    if name and skills:

        print(f'Hello {name} This Is Your Score Table:')

        for skill, score in  skills.items():

            print(f'{skill} => {score}')

    elif name and not skills :

        print(f'Hello {name} You Have No Scores To Show')

    elif not name and skills:

        for skill, score in skills.items():

            print(f'{skill} => {score}')

        return
    
    for skill, value in skills.items():

        print(f"Hello {name} Your Skills Are: ")

        print(f'- {skill} => {value}')

get_people_scores("Diaa", Python = 90)

print('=' * 50)

# ==================== Assignment 07 ====================

scores = {
    "Math" : "90",
    "Science" : "80",
    "Language" : "70"
}

def get_the_scores(name = "", **score_list):

    if name and score_list:

        print(f"Hello {name} This Is Your Score Table:")

        for key, value in score_list.items():

            print(f'{key} => {value}')

    elif name and not score_list:

        print(f'Hello {name} You Have No Scores To Show')

    elif not name and score_list:

        for subject, score in score_list.items():

            print(f'{subject} => {score}')


get_the_scores("Diaa", **scores)

print("=" * 20)

get_the_scores("Osama")

print("=" * 20)

get_the_scores(**scores)

print('*' * 100)