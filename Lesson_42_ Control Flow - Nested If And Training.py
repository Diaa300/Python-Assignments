# ----------------
# ---Nested if ---
# ----------------

Your_Name = "Diaa"
isStudent = "Yes"
Your_Country = "Egypt"
Course_Name = "Python Course"
Course_Price = 100



if Your_Country == "Egypt" or Your_Country == "KSA" or Your_Country == "Qatar":
     
     if isStudent == "Yes" :
        print(f"Hello {Your_Name} Because You From {Your_Country} And Student")
        print(f"\"{Course_Name}\" Price Is: ${Course_Price - 90}")
     else :
         
         print(f"\"{Course_Name}\" Price Is: ${Course_Price - 80}")



elif Your_Country == "Kuwait" or Your_Country == "Bahrain" :

    print(f"Hello {Your_Name} Because You From {Your_Country}")
    print(f"\"{Course_Name}\" Price Is: ${Course_Price - 50}")

else :
     print(f"Hello {Your_Name} Because You From {Your_Country}")
     print(f"\"{Course_Name}\" Price Is: ${Course_Price - 30}")

