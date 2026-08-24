import os 

os.makedirs("Python")

file = open(r"D:\Python_Course\Python\assign.py", "x")

for i in range(1, 51) :

    if i == 25:

        f = open("Python/special-text.txt", "w")
        f.close()

    else :

        f = open(f"Python/txt{i}.txt", "w")
        f.write(f"Elzero Web School => {i}\n")
        f.close()


print(os.getcwd()) 
print(os.path.abspath("Python")) 
print("assign.py") 
print(len(os.listdir("Python")))

file = open("Python/txt1.txt", "a")

for i in range(50):

    file.write("Appended => Elzero Web School\n")

file.close()

f = open("Python/txt1.txt", "r")
content = f.read()
f.close()

print(f'Number Of Lines Is => {len(content.splitlines())}')
print(f'Number Of Words Is => {len(content.split())}')
print(f'Number Of Chars Is => {len(content)}')
print(f'Number Of "l" Char Is => {content.count("l")}') 

for i in range(41, 51):
    os.remove(f"Python/txt{i}.txt")