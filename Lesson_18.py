# --------------------------------
# -- String Formatting New Ways --
# --------------------------------

name = "Diaa"
age = 16
rank = 7

# print ("My Name Is : " + name + "And My Age Is: "+ age )
print ("My Name Is: {}" .format(name) +" And My Age Is: {}".format(age))
# print ("My Name Is: %s And My Age Is: %d "%(name,age))
print ("My Name Is: {} And My Age Is: {} And My Rank Is: {:.2f}".format(name,age,rank))

# {:S} => String
# {:d} => Number
# {:f} => Float

n = "Diaa"
l = "Python"
w = 2
print ("My Name Is {:s} Iam {:s} Develober With {:d} weeks EXP ".format(n, l, w))

# Control Floating Point Number
Mynumber = 10
print ("My Number Is: {:d}" .format(Mynumber))
print ("My Number Is: {:.1f}" .format(Mynumber))

# Truncate String

mylongstring = "Hello Peoples of alzero web school I Love You All"
print ("Message Is: {:s}".format(mylongstring))
print ("Message Is: {:.34s}".format(mylongstring))

# Format Money

mymoney = 512365487878 
print ("My Money In Bank Is: {:d}".format(mymoney))
print ("My Money In Bank Is: {:,d}".format(mymoney))
print ("My Money In Bank Is: {:_d}".format(mymoney))

# ReArrange Items 

a, b, c = "One", "Two", "Three"
print ("Hello {} {} {}".format(a, b, c)) # Hello One Two Three
print ("Hello {2} {0} {1}".format(a, b, c)) # Hello Three One Two
print ("Hello {2} {1} {0}".format(a, b, c)) # Hello Three Two One

x, y, z = 10, 20 ,30
print ("Hello {} {} {}".format(x, y, z)) # Hello 10 20 30
print ("Hello {2:d} {0:d} {1:d}".format(x, y, z)) # Hello 30 10 20
print ("Hello {2:f} {1:f} {0:f}".format(x, y, z)) # 
print ("Hello {2:.2f} {1:.1f} {0:.3f}".format(x, y, z)) # 

# Format Variable in version 3.6+

myname = "Diaa"
age = 16
print ("My Name is: {myname} and My Age is: {age}") # My Name is: {myname} and My Age is: {age} 
print (f"My Name is: {myname} and My Age is: {age}") # My Name is: Diaa and My Age is: 16
