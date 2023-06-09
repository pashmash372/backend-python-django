# truthy and falsy values

a = None
#  what is None? None is a special value in Python that represents the absence of a value
#  what is the type of None? NoneType (None is the only value of NoneType)
# what is the value of None? None
# what is the bool value of None? False
# what is the bool value of 0? False
# what is the bool value of 1? True
# what is the bool value of 2? True
# what is the bool value of -1? True
# what is the bool value of 0.0? False
# what is the bool value of 0.1? True
# what is the bool value of 0.0 + 0.0j? False
# what is the bool value of 0.1 + 0.0j? True


# what is the bool value of "": False
# what is the bool value of " ": True
# what is the bool value of "0": True
# what is the bool value of "1": True
# what is the bool value of "False": True
# what is the bool value of "None": True
# what is the bool value of "True": True

# what is the bool value of []: False
# what is the bool value of [None]: True
# what is the bool value of [0]: True
# what is the bool value of [1]: True
# what is the bool value of [False]: True
# what is the bool value of [True]: True
# what is the bool value of [0, 1, 2]: True
# what is the bool value of [0, 1, 2, None]: True

# what is the bool value of (): False
# what is the bool value of (None,): True
# what is the bool value of (0,): True
# what is the bool value of (1,): True
# what is the bool value of (False,): True
# what is the bool value of (True,): True
# what is the bool value of (0, 1, 2): True

# what is the bool value of {}: False
# what is the bool value of {None: None}: True
# what is the bool value of {0: 0}: True

# what is the bool value of set(): False
# what is the bool value of {None}: True
# what is the bool value of {0}: True
# what is the bool value of {1}: True
# what is the bool value of {False}: True

# what is the bool value of range(0): False
# what is the bool value of range(1): True
# what is the bool value of range(2): True
# what is the bool value of range(0, 0): False
# what is the bool value of range(0, 1): True
# what is the bool value of range(0, 2): True
# what is the bool value of range(1, 1): False
# what is the bool value of range(1, 2): True
# what is the bool value of range(1, 3): True

# what is the bool value of range(0, 0, 1): False
# what is the bool value of range(0, 1, 1): False
# what is the bool value of range(0, 2, 1): True
# what is the bool value of range(1, 1, 1): False
# what is the bool value of range(1, 2, 1): True

# Null in python is None
# Null in Java is null

a = None
if a:
    print("a is not None")
else:
    print("a is None")

if a != None:
    print("a is not None")
else:
    print("a is None")

print(bool(a))

print(bool(2))


empyt_collection = []

if empyt_collection: # what is the name of this syntax? truthy and falsy values
    print("Collection is not empty")
else:
    print("Collection is empty")

# what is the output of the above code ? Collection is empty

print(bool(empyt_collection))