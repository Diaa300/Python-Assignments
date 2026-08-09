# ------------------
# -- Loop => While Training --
# ------------------

# while condition_is_true
#   Code Will Run Until Condition Become False
# ------------------

import time

My_Friends = ["Diaa", "Kadre", "Ahmed", "ElSayed", "Ragab", "Mohamed", "Magdy", "Adham", "Ebrahim", "Ali", "Mahmoud"]

print(len(My_Friends)) # List Length

a = 0

while a < len(My_Friends) : # a < 11

    print(f"#{str (a + 1).zfill(2)} {My_Friends[a]}")
    a += 1 # a = a + 1 
    time.sleep(0.5)

else :

    print("\n""All Friends Printed")



# print(My_Friends[0])
# print(My_Friends[1])
# print(My_Friends[2])
# print(My_Friends[3])
# print(My_Friends[4])
# print(My_Friends[5])
# print(My_Friends[6])
# print(My_Friends[7])
# print(My_Friends[8])
# print(My_Friends[9])
# print(My_Friends[10])