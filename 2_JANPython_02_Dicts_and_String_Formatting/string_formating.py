# formating strings - pythonic way
# - Bad way - string concatenation
# - old way - string % operator
# - new way - str.format()
# - new new way - f-strings

first_name = "John"
customer_count = 1000
my_message = "Hello, " + first_name + " you are customer number " + str(customer_count)

# integer to string conversion is required  - str(customer_count)

print(my_message)  # Hello, John you are customer number 1000

#  %s - string , %d - integer , %f - float , %2f - float with 2 decimal places


my_message = "Hello, %s you are customer number %d" % (first_name, customer_count)

print(my_message)  # Hello, John you are customer number 1000

# %f - float , %2f - float with 2 decimal places example

my_message = "Hello, %s you are customer number %d and you have spent %.2f" % (first_name, customer_count, 100.123456)

print(my_message)  # Hello, John you are customer number 1000 and you have spent 100.12

my_message = "Hello, %s you are customer number %d and you have spent %.2f" % (
    first_name, customer_count, 100.123456)  # \ - escape character

print(my_message)  # Hello, John you are customer number 1000 and you have spent 100.12

my_message = "Hello, %s you are customer number %d and you have spent %.2f"
my_message = my_message % (first_name, customer_count, 100.123456)

print(my_message)  # Hello, John you are customer number 1000 and you have spent 100.12

# why the above method is bad ? - because it is not readable and it is not pythonic way of doing things - it is old
# way of doing things    - it is not recommended


# new way - str.format()

my_message = "Hello, {} you are customer number {} and you have spent {}".format(first_name, customer_count, 100.123456)

# named indexes:

message_template = "My name is {fname} {lname} and I am {age} years old"

message_one = message_template.format(fname="John", lname="Doe", age=20)

print(message_one)  # My name is John Doe and I am 20 years old

# numbered indexes:
message_two = "My name is {0}, I have {1} years and I am from {2}".format("John", 20, "USA")

print(message_two)  # My name is John, I have 20 years and I am from USA

# empty placeholders:

message_three = "My name is {}, I have {} years and I am from {}".format("John", 20, "USA")

print(message_three)  # My name is John, I have 20 years and I am from USA

name = "varun"
experience = 10

print(f"Hello, {name} you have {experience} years of experience")  # Hello, varun you have 10 years of experience

#  explain the above code in detail


# f-strings - python 3.6 and above

# f-strings are faster than str.format() and % operator
# f-strings are more readable than str.format() and % operator
# f-strings are more pythonic than str.format() and % operator


fname = "Ajay"
work_experience = 10
message_template_first_way = "Hello, {fname} you have {work_experience} years of experience"
message_template_second_way = f"Hello, {fname} you have {work_experience} years of experience"

print(message_template_first_way)  # Hello, {fname} you have {work_experience} years of experience
print(message_template_first_way.format(fname=fname,
                                        work_experience=work_experience))  # Hello, Ajay you have 10 years of experience
message_template_first_way.format(fname=fname, work_experience=work_experience) # Hello, Ajay you have 10 years of experience



print(message_template_second_way)  # Hello, Ajay you have 10 years of experience
