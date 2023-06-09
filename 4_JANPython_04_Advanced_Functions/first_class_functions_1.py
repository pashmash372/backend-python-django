
"""
def special_print(func):
    # print is just for example - could involve a bunch of pre and post steps
    print("Do some preparation before fetching the result")
    func()
    print("Do some cleanup after fetching the result", end="\n\n")


def source_x():
    print("Fetching data from source x")


def source_y():
    print("Fetching data from source y")


special_print(source_x)
# Do some preparation before fetching the result
# Fetching data from source x
# Do some cleanup after fetching the result


special_print(source_y)
# Do some preparation before fetching the result
# Fetching data from source y
# Do some cleanup after fetching the result


# this is DRY    - Don't Repeat Yourself - we are repeating the same code in both the functions - we can avoid this by using a decorator

"""


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

def filter_vowels(letter):
    vowels=['a','e','i','o','u']
    return  True if letter in vowels else False

filter_vowels=filter(filter_vowels,letters) # filter object     - this is a lazy object - it is not evaluated until we iterate over it

print(filter_vowels) # <filter object at 0x0000020F4F4F7D90>

# converting to list
vowels=list(filter_vowels)
print(vowels) # ['a', 'e', 'i', 'o', 'u']


# converting to tuple
vowels=tuple(filter_vowels)
print(vowels) # ('a', 'e', 'i', 'o', 'u')

# generate filtered example using list comprehension
vowels=[letter for letter in letters if letter in ['a','e','i','o','u']]
print(vowels) # ['a', 'e', 'i', 'o', 'u']

# generate filtered example using filter function
vowels=filter(lambda letter: True if letter in ['a','e','i','o','u'] else False,letters)

