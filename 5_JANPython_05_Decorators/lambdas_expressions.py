# Lambda Functions

# Lambda functions are anonymous functions that are created using the lambda keyword.

def my_square_name(input_one):
    return input_one **2

square = lambda x: x ** 2
print(square(5))


lambda_func = lambda x:True if x**2 >= 10 else False

print(lambda_func(3))
print(lambda_func(5))

# filter(function, iterable)
# sorted(collection,key)

my_dict={'A':6,'B':2,'C':4,'D':3,'E':5}
# sorted(my_dict,key=lambda x:x[1],reverse=True)
print(sorted(my_dict, key=lambda x: my_dict[x] % 3))
print(sorted(my_dict, key=lambda x: my_dict[x] % 2))

# print(my_dict)

