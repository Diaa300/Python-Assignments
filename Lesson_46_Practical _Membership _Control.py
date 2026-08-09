# ------------------------------------
# --- Practical Membership Control ---
# ------------------------------------

# Admins
admins = ["Diaa", 'Mohamed', 'Kadre', "Ahmed"]

# Login
name = input("Please Type Your Name. ").strip().capitalize()

# If Name Is In Admin

if name in admins :

    print(f'Hello {name} Welcome Back')

    option = input("Delete Or Update Your Name? ").strip().capitalize()

    print(option)

    # Update Option

    if option == "Update" :

        theNewName = input('Your New Name Please. ').strip().capitalize()

        admins[admins.index(name)] = theNewName
        print("Name Updated. ")

        print(admins)

    # Delete Option        

    elif option == "Delete" :

        admins.remove(name)

        print ("Name Deleted") 

        print(admins)

    # Worng Option

    else :
        print("Worng Option ")

else :

    status = input("Not Admin Add You Yes, No ? ").strip().capitalize()

    if status == "Yes" or status == "Y" :

        print("You Have Been Added ")
        admins.append(name)

        print(admins)

    else :
        print("You Are Not Added. ")

