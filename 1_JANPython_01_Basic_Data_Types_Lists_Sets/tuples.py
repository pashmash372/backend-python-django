my_tuple =()

my_neighbour_tuple = ("Pakistan","China","Nepal","Bhutan","Sri Lanka")

# immutable tuple - cannot be changed / modified
# mutable list - can be changed / modified

print(my_neighbour_tuple[0])

my_neighbour_tuple[0] = "USA"   # error     # immutable tuple - cannot be changed / modified

# tuples are faster than lists - because they are immutable
#  why are tuples faster than lists? - because they are immutable
# tuples mostly used for data integrity - data that should not be changed    - like a list of countries
# tuples used in configuration files - data that should not be changed
# tuples used in database connections - data that should not be changed

# tuples used in dropdowns - data that should not be changed


new_tuple =([1,2,3],"a","b","c")  # tuple of lists

print(new_tuple[0][1])  # 2
print(new_tuple[0][1] + 1)  # 3 why but tuple is immutable? - because the list inside the tuple is mutable

new_tuple[0]= [1,2,3,4]  # error - tuple is immutable