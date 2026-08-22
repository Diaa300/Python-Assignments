# ----------------------------------
# -- Files Handling => Read Files --
# ----------------------------------
myFile = open(r"D:\Python_Course\diaa.txt ", "r")

# print(myFile)
# print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)

# print(myFile.read(5))
# print(myFile.read())
# print(myFile.read()) 

# print(myFile.readline())
# print(myFile.readline(50))
# print(type(myFile.readline())) 


for line in myFile:

    print(line)

    if line.startswith("07"):

        break

# Close The File

myFile.close()        