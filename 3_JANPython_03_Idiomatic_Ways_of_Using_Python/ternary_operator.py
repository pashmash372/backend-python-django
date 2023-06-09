# ternary operator

import random


# x= random.randint(80, 200)
# if x >100:
#     message = "Greater than 100"
# else:
#     message = "Less than 100"
#
# print(x, message)

def is_value_gt_100():  # what is the name syntax? function definition
    x = random.randint(80, 200)
    return "Value is greater than 100" if x > 100 else "Value is less than 100"


print(is_value_gt_100())

# x = random.randint(80, 200)
# y = random.randint(80, 200)
# z = random.randint(80, 200)

x, y, z = random.randint(80, 200), random.randint(80, 200), random.randint(80, 200)  # tuple unpacking and assignment
print(x, y, z)

if x < y < z:  # x < y and y < z what is the called? chaining comparison operators
    print("Y is between x and z")
else:
    print("Y is not between x and z")


def my_function():
    # do some computation or some processing
    return 1, "Two", False


x, y, z = my_function()  # tuple unpacking and assignment
print(x, y, z)
