import math
def my_decorator(func):
    def wrapper(n):
        print("Befor fun")        
        func(n)
        print("After fun")
    return wrapper

@my_decorator
def say_hello(n):
    print("Hello!")
    ans = math.factorial(n)
    print(ans)
    
say_hello(9)