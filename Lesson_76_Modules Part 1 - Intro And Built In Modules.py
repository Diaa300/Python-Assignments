# ---------------------------------
# -- Module => built In Function --
# ---------------------------------

import random

print(f'Print Random Float Number {random.random()}')

# Show All Function Inside Module 

# print(dir(random))

# Import One Or Two Functions From Module 

from random import randint , random

print(f'Print Random Float {random()}')
print(f'Print Random Integer {randint(15, 91)}')