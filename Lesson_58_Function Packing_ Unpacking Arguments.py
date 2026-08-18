# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------

def say_hello(*people) :

    for name in people:

        print(f'Hello {name}')

say_hello("Diaa", "Kadre", "Mohamed")

print('=' * 50)

def show_details(name, *skills) :

    print(f'Hello {name} Your Skills Is: ')

    for skill in skills:

        print(skill)


show_details("Diaa", "CSS", "JS", "HTML", "Python""\n")
show_details("Magdy", "CSS", "JS", "HTML", "PHP", "MySQL", "Data Science")