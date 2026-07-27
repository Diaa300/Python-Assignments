# --------------------------------
# -- String Formatting Old Ways --
# --------------------------------

name = "Diaa"
age = 16
rank = 7
# print ("My Name Is : " + name + "And My Age Is: "+ age )
print ("My Name Is: %s" % name +" And My Age Is: %s" % age)
print ("My Name Is: %s And My Age Is: %d "%(name,age))
print ("My Name Is: %s And My Age Is: %d And My Rank Is: %f"%(name,age,rank))

# %S => String
# %d => Number
# %f => Float

n = "Diaa"
l = "Python"
y = 10
print ("My Name Is %s Iam %s Develober With %d Years EXP "% (n, l, y))

# Control Floating Point Number
Mynumber = 10
print ("My Number Is: %d"% Mynumber)
print ("My Number Is: %.1f"% Mynumber)

# Truncate String

mylongstring = "Hello Peoples of alzero web school I Love You All"
print ("Message Is: %s"% mylongstring)
print ("Message Is: %.34s"% mylongstring)