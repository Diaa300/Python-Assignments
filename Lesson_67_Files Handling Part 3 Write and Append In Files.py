# ------------------------------------------------
# -- Files Handling => Write and Append In File --
# ------------------------------------------------

# myFile = open(r"D:\Python_Course\diaa.txt", "w")
# myFile.write("Hello From Python Files With Love\n")
# myFile.write("Second Line")

# myFile = open(r"D:\Python_Course\fun.txt", "w")
# myFile.write("Elzero Web School\n" * 1000)

# myList = ["Diaa\n", "Ahmed\n", "Kadre\n"]

# myFile= open(r"D:\Python_Course\diaa.txt", "w")
# myFile.writelines(myList)

myFile = open(r"D:\Python_Course\diaa.txt", "a")
myFile.write("Here Is A new Line\n")
myFile.write("Third Line")