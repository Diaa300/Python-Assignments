# ==================== Assignment 01 ====================

tries = 4

Password = "123456"

inputPassword = input('Write Your Password: ')

while inputPassword != Password :

    tries -= 1

    print(f"Wrong Password, {'Last' if tries == 0 else tries} Chances Left. ")

    inputPassword = input('Write Your Password: ')

    if tries == 0:

        print("All Tries Is Finished")

        break

else:

    print("Correct Password")

print("=" * 100)

# ==================== Assignment 02 ====================

