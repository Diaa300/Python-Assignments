# # -------------
# # التكليف الأول
# # -------------

print(bool(1))
print(bool([1, 2, 3, 4, 5]))
print(bool(True))
print(bool("Diaa"))

print(bool({}))
print(bool(""))
print(bool(False))
print(bool(0))

print('#' * 50)

# التكليف الثاني

html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50)

print('#' * 50)

# التكليف الثالث

num_one = 10
num_two = 20
num = 20

print(num > num_one) != (num > num_two)
print(num > num_one and num > num_two)

print("#" * 50)

# التكليف الرابع

num_one = 10
num_two = 20

result = num_one + num_two
print(result)

result = result ** 3
print(result)

result = result % 26000
print(result)

result = result / 5
print(result)

result = str(result)
print(type(result))

print("#" * 50)

# التكليف الخامس

name = input("What's Your Name? ").strip().capitalize()
print(f"Hello {name}, Happy to See You Here")

print("#" * 50)

# التكليف السادس

age = int(input("What's Your Age? ").strip())
messages = [
    "Hello Your Age Is Under 16, Some Articles Is Not Suitable For You",
    f"Hello Your Age Is {age}, All Articles Is Suitable For You"
]
print(messages[age >= 16])

print('#' * 50)

# التكليف السابع

FirstName = input("What's Your First Name? ").strip().capitalize()
SecondName = input('What\'s Your Second Name? ').strip().capitalize()

print(f"Hello {FirstName} {SecondName[0]}")

print("#" * 50)

# التكليف الثامن

email = input("What's Your Email? ").strip().lower()

YourName = email [:email.index("@")].capitalize()
EmailService = email [email.index("@") + 1:email.index(".")]
TopLevelDomain = email [email.index(".") + 1:]

print(f"Your Name Is {YourName}")
print(f"Email Service Provider Is {EmailService}")
print(f"Top Level Domain Is {TopLevelDomain}")

print("@" * 100)