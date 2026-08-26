# -----------------------------------
# --  Built In Functions => Reduce --
# -----------------------------------

from functools import reduce

def sumAll(num1, num2):

    return num1 + num2

numbers = [1, 2, 3, 4, 5, 6, 8, 9]

# result = reduce(sumAll, numbers)
result = reduce(lambda num1, num2: num1 + num2, numbers)

print(result)