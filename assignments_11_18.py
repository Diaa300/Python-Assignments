name= "Diaa"
age = 16
country = "Egypt"

print ("Hello '"+ name +"',How You Doing \\ \n \"\"\" Your age is\"" + str(age) + "\"\"\" + \nAnd your Country Is: " + country)

# -----------------------------

name = 'ELzero'

print ('Second Letter Is "' + name[1] + '"')
print ('Third Letter Is  "' + name[2] + '"')
print ('Last Letter Is "'  + name[-1] + '"')

# --------------------------------

print ('"' + name[1:4] + '"')
print ('"' + name[0:5:2] + '"')
print ('"' + name[-2:-7:-2] + '"')

# ---------------------------------

name = "#@#@Elzero#@#@"

print (name.strip("#@"))

# ------------------------------------

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print (num1.zfill(4))
print (num2.zfill(4))
print (num3.zfill(4))
print (num4.zfill(4))
print (num5.zfill(4))

# ---------------------------------------------------

name_one = "Osama"
name_two = "Osama_Elzero"

print (name_one.rjust(20,"@"))
print (name_two.rjust(20,"@"))

# -------------------------------------------------------------

name_one = "OSamA"
name_two = "osaMA"

print (name_one.swapcase())
print (name_two.swapcase())

# -----------------------------------------------------------------------

msg = "I Love Python And Although Love Elzero Web School"

print  (msg.count("Love"))

# -----------------------------------------------------------------------------------

name = "Elzero"

print (name.find("z"))

# _____________________________________________________________________________________________

msg = "I <3 Python And Although <3 Elzero Web School"

print (msg.replace("<3","Love",1))

# ----------------------------------------------------------------------------------------------------------

msg = "I <3 Python And Although <3 Elzero Web School"

print (msg.replace("<3","Love"))

# _____________________________________________________________________________________________________________________

name = "Diaa"
age = 16
country = "Egypt"

print (f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}") 