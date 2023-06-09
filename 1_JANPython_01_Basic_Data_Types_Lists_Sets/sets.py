
# sets

# A set is an unordered collection of items.
# Every element is unique (no duplicates) and must be immutable (which cannot be changed).

# However, the set itself is mutable. We can add or remove items from it.

# Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.

# set of integers
my_set = {1, 2, 3}
print(my_set)  # {1, 2, 3}

# set of mixed datatypes

my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)  # {1.0, 'Hello', (1, 2, 3)}

# set cannot have duplicates

my_set = {1, 2, 3, 4, 3, 2}  # duplicates are not allowed

print(my_set)  # {1, 2, 3, 4}

# we can make a set from a list

my_set = set([1, 2, 3, 2])

print(my_set)  # {1, 2, 3}

# initialize a set with set() method

my_set = set()

print(my_set)  # set()

# no duplicates allowed

my_set = {}

my_favorite_fruits = {"apple", "banana", "orange", "apple", "pear", "banana", "orange"}

print(my_favorite_fruits)  # {'banana', 'pear', 'orange', 'apple'}

my_set.add(1)
my_set.add(222)
my_set.add(333)
my_set.update([5, 6, 0, 11, 1])

print(my_set)  # {1, 333, 5, 6, 11, 222, 0}

# unindexed - no index numbers

for item in my_set:
    print(item)  # 0 1 333 5 6 11 222

# unordered - no order of elements

# why set is faster explain in detail  - because set is unordered and unindexed - so it is faster to search

# elements are immutable  , set is mutable


# set operations

# union

# intersection

# difference

# symmetric difference

# union

# union of A and B is a set of all elements from both sets.

# union is performed using | operator. Same can be accomplished using the method union().

# initialize A and B

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator

print(A | B)  # {1, 2, 3, 4, 5, 6, 7, 8}

# use union function

print(A.union(B))  # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection

# intersection of A and B is a set of elements that are common in both sets.

# intersection is performed using & operator. Same can be accomplished using the method intersection().

# initialize A and B

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator

print(A & B)  # {4, 5}

# use intersection function

print(A.intersection(B))  # {4, 5}

# difference


# difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly, B - A is a set of element in B but not in A.

# difference is performed using - operator. Same can be accomplished using the method difference().

# initialize A and B

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A

print(A - B)  # {1, 2, 3}

# use difference function on A


print(A.difference(B))  # {1, 2, 3}

# symmetric difference

# symmetric difference of A and B is a set of elements in both A and B except those that are common in both.

# symmetric difference is performed using ^ operator. Same can be accomplished using the method symmetric_difference().
# initialize A and B

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator

print(A ^ B)  # {1, 2, 3, 6, 7, 8}

# use symmetric_difference function on A

print(A.symmetric_difference(B))  # {1, 2, 3, 6, 7, 8}

# set methods

# add() - Adds an element to the set

# clear() - Removes all elements from the set

# copy() - Returns a copy of the set

# difference() - Returns the difference of two or more sets as a new set


# difference_update() - Removes all elements of another set from this set

# discard() - Removes an element from the set if it is a member. (Do nothing if the element is not in set)

# intersection() - Returns the intersection of two sets as a new set

# intersection_update() - Updates the set with the intersection of itself and another

# isdisjoint() - Returns True if two sets have a null intersection

# issubset() - Returns True if another set contains this set

# issuperset() - Returns True if this set contains another set



# pop() - Removes and returns an arbitary set element. Raise KeyError if the set is empty

# remove() - Removes an element from the set. If the element is not a member, raise a KeyError

# symmetric_difference() - Returns the symmetric difference of two sets as a new set

# symmetric_difference_update() - Updates a set with the symmetric difference of itself and another

# union() - Returns the union of sets in a new set

# update() - Updates the set with the union of itself and others

# frozenset() - Returns a new frozenset object from the given iterable


# Python Frozenset

# Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.

# Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.

# Frozensets can be created using the function frozenset().

# This datatype supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union(). Being immutable it does not have method that add or remove elements.

# Frozensets can be created using the frozenset() function.


# set usecases

# set is used to remove duplicates from a list

# set is used to perform mathematical operations like union, intersection, symmetric difference etc.

# set is used to check membership in a set

# set is used to remove duplicates from a list


