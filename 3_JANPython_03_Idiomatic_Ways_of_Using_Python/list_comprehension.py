# what is idiomatic python?

# 1. use list comprehension instead of map and filter
list_of_amounts = [100, 200, 300, 400, 500, 800, 2000, 100, 120, 560]

# list_of_amounts_gt_hundred = []
#
# for amount in list_of_amounts:
#     if amount > 100:
#         list_of_amounts_gt_hundred.append(amount)
#
# print(list_of_amounts_gt_hundred) # [200, 300, 400, 500, 800, 2000, 120, 560]


list_of_amounts_gt_hundred = [amount for amount in list_of_amounts if amount > 100]

print(list_of_amounts_gt_hundred)  # [200, 300, 400, 500, 800, 2000, 120, 560]

list_of_amounts_gt_hundred = [f"Rs. {amount}" for amount in list_of_amounts if amount > 100]

print(list_of_amounts_gt_hundred)
# ['Rs. 200', 'Rs. 300', 'Rs. 400', 'Rs. 500', 'Rs. 800', 'Rs. 2000', 'Rs. 120', 'Rs. 560']


amount_value_gt_500 = [amount - 500 for amount in list_of_amounts if amount > 500]

print(amount_value_gt_500)  # [300, 500, 1500, 60]

first_10_real_numbers = [number for number in range(1, 11)]

print(first_10_real_numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sq_of_first_10_integer_numbers = [i ** 2 for i in first_10_real_numbers]

print(sq_of_first_10_integer_numbers)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list_of_amounts = [100, 200, 300, 400, 500, 800, 2000, 100, 120, 560]

final_result = [amount if amount > 500 else 0 for amount in list_of_amounts]
# what is the name of this syntax?
# explain the above line
# 1. if amount > 500:
#       final_result.append(amount)
#    else:
#       final_result.append(0)

print(final_result)  # [0, 0, 0, 0, 500, 800, 2000, 0, 0, 560]

# 2. use enumerate instead of range(len())

# 3. use zip instead of iterating over indices

# 4. use dict.get() to retrieve value from dict

# 5. use dict comprehension to create dict
