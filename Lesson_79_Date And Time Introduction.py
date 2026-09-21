# -----------------------------------
# -- Date And Time => Introduction --
# -----------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

print(datetime.datetime.now())

print("#" * 50)

# Print The Current Year
print(datetime.datetime.now().year)

# Print The Current Month
print(datetime.datetime.now().month)

# Print The Current Day
print(datetime.datetime.now().day)

# Print Start And End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

mybirthday = datetime.datetime(2010, 6, 5)
datenow = datetime.datetime.now()

print(f'My Birthday Is {mybirthday} And', end="")
print(f'Date Now Is {datenow}')

print(f'I Lived For {(datenow - mybirthday).days} Days.')