# list_of_shoes=[] # empty list

list_of_shoes = ["addidas", "nike", "puma", "reebok", "fila", "asics", "converse", "vans", "new balance", "skechers"]

list_of_spends = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# print(list_of_spends) # [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

list_of_arbitrary_things = ["varun", "Delhi", 10, ["Python", "Java", "C++", "C#"], True, 10.5]  # list of lists

# print(list_of_arbitrary_things[3][2]) # C++


# slicing   [start:stop:step]   start is inclusive, stop is exclusive   step is optional and default is 1

# default slicing
# start -0
# stop - n (element not included)
# step - 1
# print(list_of_shoes[0:5:2])
# print(list_of_shoes[::])
# print(list_of_shoes[::-1])

enumerate_list = list(enumerate(list_of_shoes))
print(enumerate_list)  # [(0, 'addidas'), (1, 'nike'), (2, 'puma'), (3, 'reebok'), (4, 'fila'), (5, 'asics'), (6,
# 'converse'), (7, 'vans'), (8, 'new balance'), (9, 'skechers')]
print(list_of_shoes[0:8:2])  # ['addidas', 'puma', 'fila', 'converse']

print(list_of_shoes[1:7])  # ['nike', 'puma', 'reebok', 'fila', 'asics', 'converse']

# negative index slicing - start from the end of the list and go backwards  -1 is the last element of the list

print(list_of_shoes[-1])  # skechers

print(list_of_shoes[-1:-5:-1])  # ['skechers', 'new balance', 'vans', 'converse']

print(list_of_shoes[-1:-5])  # []

print(list_of_shoes[-5:-1])  # ['fila', 'asics', 'converse', 'vans']

print(list_of_shoes[-5:])  # ['fila', 'asics', 'converse', 'vans', 'new balance', 'skechers']

print(list_of_shoes[:-5])  # ['addidas', 'nike', 'puma', 'reebok', 'fila']

print(list_of_shoes[-5:-1:2])  # ['fila', 'converse']

print(list_of_shoes[-1:-5:-2])  # ['skechers', 'vans']

print(list_of_shoes[-1:-5:2])  # []

print(list_of_shoes[-1:-5:-2])  # ['skechers', 'vans']

print(list_of_shoes[-1:-5:-3])  # ['skechers', 'converse']

print(list_of_shoes[-1:-5:3])  # []

print(list_of_shoes[-1:-5:-4])  # ['skechers']

print(list_of_shoes[-1:-5:4])  # []

print(list_of_shoes[-1:-5:-5])  # ['skechers']

print(list_of_shoes[-1:-5:5])  # []

print(list_of_shoes[-1:-5:-6])  # ['skechers']

print(list_of_shoes[-1:-5:6])  # []

print(list_of_shoes[-1:-5:-7])  # ['skechers']

print(list_of_shoes[0:5:2])  # ['addidas', 'puma', 'fila', 'converse']

print(list_of_shoes[0:5:-2])  # []

print(list_of_shoes[0:5:3])  # ['addidas', 'reebok']

print(list_of_shoes[0:5:-3])  # []

print(list_of_shoes[0:5:4])  # ['addidas', 'fila']

print(list_of_shoes[0:5:-4])  # []

print(list_of_shoes[0:5:5])  # ['addidas']

print(list_of_shoes[0:5:-5])  # []

print(list_of_shoes[0:5:6])  # ['addidas']

print(list_of_shoes[0:5:-6])  # []

print(list_of_shoes[0:5:7])  # ['addidas']

print(list_of_shoes[0:5:-7])  # []

print(list_of_shoes[0:5:8])  # ['addidas']

print(list_of_shoes[0:5:-8])  # []

print(list_of_shoes[0:5:9])  # ['addidas']

print(list_of_shoes[0:5:-9])  # []
