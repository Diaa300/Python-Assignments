# -------------------------------------------------------
# ----- Calculate Age Advanced Version and Training -----
# -------------------------------------------------------

# Write Note

print("#" * 100)
print("You Can Write The Frist Letter Or Full Name Of The Time Unit".center(100, "#")) 
print("#" * 100 + "\n")

# Collect Age Data

age = input("Please write Your Age ").strip()

# Collect Time Unit Data 

unit = input("Please Choose Time Unit: Months, Weeks, Days ").strip().lower()

# Get Time Units

months = int(age) * 12
weeks = months * 4
days = int(age)* 365

if unit == "months" or unit == "m" :
    print("You Choose The Unit Months")
    print(f"You Lived For {months:,} Months.")

elif unit == "weeks" or unit == "w" :
    print("You Choose The Unit Weeks")
    print(f"You Lived For {weeks} weeks.")

elif unit == "days" or unit == "d":
    print("You Choose The Unit Days")
    print(f"you Lived For {days} Days.")

else :
    print("The Unit Not Found.")    