from time import time



def speed_test(func):

    def wrapper():

        start = time()

        func()

        end = time()

        print(f'Function Running Time Is: {end - start}')

    return wrapper


@speed_test
def bigLoop():


    for num in range(1, 1000000):

        print(num)


bigLoop()