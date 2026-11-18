# -------------------------
# -- Decorators => Intro --
# -------------------------

# [1] Decorator Is A Function That Takes Another Function As A Parameter
# [2] It Adds Some Behavior And Returns It
# [3] Sometimes Called Metaprogramming
# [4] Decorated Function Is Called Wrapper

def my_decorator(func):  # Decorator
  def nested_func():  # Any Name / Wrapper
    print("Before Message")
    func()  # Execute Function
    print("After Message")

  return nested_func()


@my_decorator
def say_hello():
  print("Hello From Diaa Ragab")


# say_hello()