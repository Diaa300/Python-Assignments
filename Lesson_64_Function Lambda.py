# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# # ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Function And Def Function The Large Task
# [5] Lambda Is One Expression Not Block Of Code
# [6] Lambda Type Is Function
# --------------------------------------------------------

def say_hello(name, age):

    return f"Hello {name} Your Age Is {age}"

hello = lambda name, age: f'Hello {name}'

print(say_hello("Ahmed", 26))
print(hello("Diaa", 16))

print(say_hello.__name__)
print(hello.__name__)

print(type(say_hello))
print(type(hello))

