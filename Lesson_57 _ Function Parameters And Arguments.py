# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------

# a, b, c, d = "Diaa", "Mohamed", "Ahmed", "Kadre"

# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")
# print(f"Hello {d}")

# def                    => Function Keyword [define]
# say_hello              => Function Name
# name                   => Parameter
# print(f"Hello{name}")  => Task 
# say_hello("Ahmed")     => Ahmed Is Argument

# def say_hello(name) :

#     print(f"Hello {name}")


# say_hello(a)
# say_hello(b)
# say_hello(c)
# say_hello(d)

# def addition(n1, n2):

#     print(n1 + n2)

# addition(100, 50)
# addition(654, 941)

def addition(n1, n2):

    if type(n1) != int or type(n2) != int:

        print("only Integers Allowed")

    else:        

        print(n1 + n2)

addition(100, 50)
addition(654, 941)



def full_name(frist, middle, last):

    print(f'Hello {frist.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}')

full_name("    Diaa   ", "ragab", 'ElSayed' )

