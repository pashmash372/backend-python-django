# decorators


# what is decorator?
# decorator is a function that takes another function as an argument, adds some kind of functionality and returns another function
# all of this without altering the source code of the original function that we passed in

# example
def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed this before {original_function.__name__}')     # __name__ is a special attribute of a function
        return original_function()
    return wrapper_function

