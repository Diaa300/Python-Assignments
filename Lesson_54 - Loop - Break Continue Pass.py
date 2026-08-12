# ---------------------------
# -- Break, Continue, Pass --
# ---------------------------


myNumber = [1, 2, 4, 6, 7, 8, 9, 11, 19, 56, 78, 98]


# Continue

for number in myNumber:

    if number == 11:

        continue

    print(number)

print("*" * 50)

# Break

for number in myNumber:

    if number == 11:

        break

    print(number)

print('#' * 50)

# Pass

for number in myNumber:

    if number == 11:

        pass

    print(number)