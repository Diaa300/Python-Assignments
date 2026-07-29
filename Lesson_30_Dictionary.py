# ----------------------
# ----- Dictionary -----
# ----------------------
# [1] Dict Items Are Enclosed in curly Braces
# [2] Dict Items Are Contains Key : Value 
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------------

user = {
    "name" : "Diaa",
    "age" : "16",
    "Country" : "Egypt",
    "Skills" : ["Html", "Css", "Js"],
    "rating" : 10.5
}

print(user)
print(user['Country'])
print(user.get("Country"))
print(user.keys())
print(user.values())

# Two-Dimensional Dictionary

languages = {
    "One" : {
        "name" : "Html",
        "progress" : "65%"
    },
    "Two" : {
        "name" : "Css",
                "progress" : "60%"
    },
    "Three" : {
        "name" : "Js",
                "progress" : "75%"
    }
}

print(languages)
print(languages["One"]["name"])
print(languages["Three"]['progress'])
print(languages["Two"])

# Dictionary Lenght

print(len(languages))
print(len(languages["One"]))
print(len(languages["Three"]))

# Creat Dictionary From Variables

frameworkOne = {
     "name" : "SQL",
    "progress" : "80%"
}

frameworkTwo = {
     "name" : "C++",
    "progress" : "90%"
}

frameworkThree = {
     "name" : "php",
    "progress" : "85%"
}

allframework = {
    "One" : frameworkOne, 
    "Two" : frameworkTwo,
    "Three" : frameworkThree
}

print(allframework)

