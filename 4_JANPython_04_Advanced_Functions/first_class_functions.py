# Functions as first class object in Python

# - created at run time
# - can be assigned to a variable
# - can be passed as function argument
# - can be returned from a function
"""
def my_new_function():
    print("Inside my new function")


my_new_variable = my_new_function

print(my_new_variable) # <function my_new_function at 0x0000020F4F4F7CA0>

print(type(my_new_variable)) # <class 'function'>

my_new_variable() # Inside my new function - this is how we call a function using a variable name - this is called as function aliasing - we can use this to call a function using a different name - we can use this to call a function using a different name - we can use this to call a function using a different name


def my_brand_new_function(func):
    func()

my_brand_new_function(my_new_function) # Inside my new function - this is how we pass a function as an argument to another function

print(my_brand_new_function) # <function my_brand_new_function at 0x0000020F4F4F7D30>

"""


def my_new_function():  # this is a function definition - we are defining a function here - we are creating a function object here  - we are creating a function object here -
    def my_inner_function():
        print("Inside my inner function")
        return "Completed execution of my inner function"
    return my_inner_function  # this is a function object


print(
    my_new_function())  # <function my_new_function.<locals>.my_inner_function at 0x0000020F4F4F7E50> - this is a function object

my_func = my_new_function()     # this is a function object
# print(my_func)
print(my_func()) # Inside my inner function - this is how we call a function object


