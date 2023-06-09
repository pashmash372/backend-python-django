# Hashmap

# dictionary is a data structure that stores data in key-value pairs
#   - keys are unique
#   - keys are immutable (cannot be changed)
#   - keys are hashable (can be converted to a number)
#   - values can be any type

# dictionaries are mutable (can be changed)

# dictionaries are unordered (cannot be indexed)

# heterogeneous (can contain different types of data)

my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}

my_dict["d"] = 4
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(my_dict["a"])  # 1

student_object = {"name": "John", "age": 16, "courses": ["Math", "CompSci"], "location": "USA",
    "subjects": ["Math", "CompSci", "English", "History"],
    "marks": {"Maths": {"mid-sem": 80, "end-sem": 90, "has_passed": True, "grade": "A"},
        "Physics": {"mid-sem": 70, "end-sem": 80, "has_passed": True, "grade": "B"

        }}}

student = [15, "John", ["Math", "CompSci"], "USA"]

print(student_object["name"])  # John

print(student[1])  # John

print(student_object["marks"]["Maths"]["mid-sem"])  # 80
print(student_object["marks"]["Physics"]["mid-sem"])  # 70
print(student_object["marks"]["Physics"]["end-sem"])

# list vs dictionary

# list - ordered, indexed, mutable, duplicates allowed, heterogeneous

# dictionary - unordered, unindexed, mutable, no duplicates, heterogeneous

# dictionary methods

# clear() - removes all elements from the dictionary

# copy() - returns a copy of the dictionary

# fromkeys() - returns a dictionary with the specified keys and values

# get() - returns the value of the specified key

# items() - returns a list containing a tuple for each key value pair
