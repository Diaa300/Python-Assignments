# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The function Can Be Pre-Defined Function Or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

# Example 1

def checknumber(num):

    if num > 10:

        return num 


myNumbers = [1, 45, 26, 19, 8, 200]

myResult = filter(checknumber, myNumbers)

for number in myResult:

    print(number)

print('#' * 50)

# Example 2

def checkName(name):

    return name.startswith("D") 


myTexts = ["Diaa", "Doha", 'Ahmed']

myResult = filter(checkName, myTexts)

for person in myResult:

    print(person)

print('#' * 50)

# Example 3


myNames = ["Diaa", "Osama", "Ahmed", "Omer", "Omar", "Othman", "Ameer"]

myReturnedname = filter(lambda name: name.startswith('A'), myNames)

for p in myReturnedname:

    print(p)
