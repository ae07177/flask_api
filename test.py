from functools import wraps

# Defining our custom decorator
def my_decorator(function):
    @wraps(function)
    def wrapper(a, b, c):
        print("wrapper running!")
        a += 1
        b += 2
        c += 3
        return function(a, b, c)
    return wrapper

# Using it to decorate a function
@my_decorator
def my_function(a, b, c):
    print "my_function running!"
    print a, b, c

my_function(a=1, b=2, c=3)
