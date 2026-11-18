# [1] Decorator With Parameters
# [2] A Decorator Can Accept Arguments For The Decorated Function Using *args and **kwargs


def my_decorator(func):
  def nested_func(*args, **kwargs):  # To accept any arguments
    print("Before Message")
    func(*args, **kwargs)  # Pass arguments to the original function
    print("After Message")

  return nested_func


@my_decorator
def calculate(n1, n2, n3):
  print(n1 + n2 + n3)


# Calling the decorated function with parameters
calculate(10, 90, 50)