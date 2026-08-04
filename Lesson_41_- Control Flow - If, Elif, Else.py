# --------------------
# -- Control Flow --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

Your_Name = input("What's Your Name? ").strip().capitalize()
Your_Country = input('What\'s Your Country? ').strip().capitalize()
Course_Name = "Python Course"
Course_Price = 100
Your_age = input('What\'s Your Age? ').strip()


if Your_age >= "16" :
    print(f"Hello {Your_Name} Your age is appropriate for this course. ")

else :
    print(f"Your age is under the required minimum")

if Your_Country == "Egypt" :
    print(f"Hello {Your_Name} Because You From {Your_Country}")
    print(f"\"{Course_Name}\" Price Is: ${Course_Price - 80}")

elif Your_Country == "KSA" :
    
    print(f"Hello {Your_Name} Because You From {Your_Country}")
    print(f"\"{Course_Name}\" Price Is: ${Course_Price - 80}")
    

else :
    print(f"Hello {Your_Name} Because You From {Your_Country}")
    print(f"\"{Course_Name}\" Price Is: ${Course_Price - 30}")



