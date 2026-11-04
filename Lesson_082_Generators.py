# ----------------
# -- Generators --
# ----------------

def myGenerator():

    yield 1
    yield 2
    yield 3
    yield 4

myGen = myGenerator()

print(next(myGen))
print(next(myGen))
print(next(myGen))

print("*" * 50)

for n in myGen:

    print(n)

print("#" * 50)

# ------------------------------
# Assignment 1 
# ------------------------------

def generate_numbers():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

gen = generate_numbers()

print(next(gen))
print(next(gen))

for g in gen:

    print(g)

print("#" * 50)

# ------------------------------
# Assignment 2
# ------------------------------

def generate_products():

    yield "Laptop"
    yield "Mouse"
    yield "Keyboard"
    yield "Monitor"
    yield "Headphones"

my_gen = generate_products()

print(next(my_gen))

for i in my_gen:

    print(i)

print("#" * 50)

# ------------------------------
# Assignment 3
# ------------------------------

def generate_orders():

    Products = {
        1 : {
            "order_id" : 101,
            "customer" : "Ahmed",
            "product" : "Laptop",
            "price" : 25000
        },

        2 : {
            "order_id" : 102,
            "customer" : "Mohamed",
            "product" : "Mouse",
            "price" : 500
        },

        3 : {
            "order_id" : 103,
            "customer" : "Ali",
            "product" : "Keyboard",
            "price" : 1200
        },

        4 : {
            "order_id" : 104,
            "customer" : "Omar",
            "product" : "Monitor",
            "price" : 6500
        },

        5 : {
            "order_id" : 105,
            "customer" : "Sara",
            "product" : "Headphones",
            "price" : 1800
        },
    }

    for order in Products.values():

        yield order


orders = generate_orders()


for order in orders:

    for key, value in order.items():

        print(f"{key}: {value}")