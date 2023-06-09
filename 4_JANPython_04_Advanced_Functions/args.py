# args

# def fun(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, name='championswimmer', age=25,
#     country='India')  # *args - positional arguments - tuple


# **kwargs - keyword arguments - dictionary
# *args - positional arguments - tuple - variable length arguments  - order matters
# **kwargs - keyword arguments - dictionary - key value pair  - variable length arguments  - order does not matter

# output of above function call
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)  # tuple
# {'name': 'championswimmer', 'age': 25, 'country': 'India'}  # dictionary


# def adder(*num):  # *name - tuple - variable length arguments - order matters - positional arguments - tuple -
#     # variable length arguments  - order matters - *args - positional arguments - tuple - variable length arguments
#     # - order matters - *args - positional arguments - tuple - variable length arguments  - order matters
#     sum = 0
#     for n in num:
#         sum = sum + n
#     print("Sum:", sum)
#
#
# adder(3, 5)  # 8
# adder(4, 5, 6, 7)  # 22
# adder(1, 2, 3, 5, 6)  # 17


"""
def adder(input_one, input_two, *num):
    print(input_one, input_two)
    print(f"Input one :{input_one}")
    print(f"Input two :{input_two}")
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:", sum)


# adder(input_one=3721, input_two=2)
adder(1, 2)
adder(1, 2, 3, 5)
"""

"""
# args - arbitrary number of input parameters to your function
# kwargs - arbitrary number of keyword arguments to your function

# kwars - keyword arguments - dictionary - key value pair  - variable length arguments  - order does not matter

def print_logs(**logs):
    for key in logs:
        print("The key {} holds {} value".format(key, logs[key]))


print_logs(name='championswimmer', age=25, country='India')

"""
# The key name holds championswimmer value
# The key age holds 25 value
# The key country holds India value

# kwargs usecases and applications
# used in backward compatibility in functions
# versions - library , utility , API


from my_library import my_email_function

# Option one - update function calls everywhere
# Option two - add a default value to the argument
# Option three - use kwargs as cc_email


"""
# Existing use of the function before the cc email input was added

my_email_function("varun@scaler.com", "Test email",
                  "Hope you are doing fine!")  # TypeError: my_email_function() missing 1 required positional argument: 'cc_email'  #  Sending email from varun@scaler with subject Test email and message Hope you are doing fine!

# New usage of the function where cc email is also provided , workable code
my_email_function("varun@scaler.com", "Test email",
                  "Hope you are doing fine!",
                  None)  # Sending email from varun@scaler with subject Test email and    message Hope you are doing fine!


# New usage of the function where cc email is also provided
my_email_function("varun@scaler.com", "Test email",
                  "Hope you are doing fine!", "ajay@scaler.com")
"""

my_email_function("varun@scaler.com", "Test email",
                  "Hope you are doing fine!", cc_email="ajay@scaler.com")
my_email_function("varun@scaler.com", "Test email",
                  "Hope you are doing fine!")


