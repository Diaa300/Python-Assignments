# -----------
# التكليف 01
# -----------


num1 = int (input("What's Your Frist Number? ").strip())
num2 = int (input("What's Your Second Number? ").strip())
operation = input("Please select the type of arithmetic operation (+ Or - Or * Or / Or %). ").strip()

if operation == "+" : 
    print (num1 + num2)

elif operation == "-" :
    print(num1 - num2)

elif operation == "*":
    print(num1 * num2)

elif operation == "/":
    print(num1 / num2) 

elif operation == "%":
    print(num1 % num2)    

else:
    print("Not Found")    


print("#" * 50)

# التكليف 02

age = int(17)

if age > 16 :
    print("App Is Suitable For You")

else :
    print("App Is Not Suitable For You")    

print("#" * 50)

# التكليف 03

Age = int (input('What\'s Your Age? '))
time_unit = input("Choose Time Unit: Months, Weeks, Days, Hours, Minutes, Seconds: ").strip().lower()


months = Age * 12
weeks = months * 4
days = Age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if 10 < age < 100: 
    print("")


    if time_unit == "month":
        print(f"You Lived For {months} Months")

    elif time_unit == "weeks":
        print(f"You Lived For {weeks} Weeks")

    elif time_unit == "days":
        print(f"You Lived For {days} Days")     

    elif time_unit == "hours":
        print(f"You Lived For {hours} Hours")    

    elif time_unit == "minutes":
        print(f"You Lived For {minutes} Minutes") 

    elif time_unit == "seconds":
        print(f"You Lived For {seconds} Seconds")        

else:
    print("Not Found")    