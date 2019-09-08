from functools import wraps

# Defining our custom decorator
def my_decorator(function):
    @wraps(function)
    def wrapper(a):
        if a == 1:
		print "I am in Wrapper Function"
        	return function(a)
	else:
		print "1 is the desired value. Very Sad"
    return wrapper

# Using it to decorate a function
@my_decorator
def my_function(a):
    print "my_function running!"
    print a

a = input("Enter Your Number:")
my_function(a)
