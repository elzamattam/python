# Differences of set from list/tuple:- unordered collection, duplicates not allowed, mutable objects not allowed inside
# Set is faster to search than list/tuple because it works on the basis of 'hashing' and 'hash tables'


# Create an empty set
set_example1 = set()
print(set_example1)


# Create a non-empty set
set_example2 = { "apple", "grape", "orange" }  
print(set_example2)


# Duplicates will be ignored
set_example3 = { "apple", "grape", "orange", "apple" }
print(set_example3)


# Convert list to set
some_list = [1, 2, 3, 1, 2, 3]
set_example4 = set(some_list)
print(set_example4)


# Add an item to set
set_example4.add(4)
print(set_example4)


# Update multiple items to set
set_example4.update([5, 6, 7])
print(set_example4)


# Remove an element
set_example4.remove(7)
print(set_example4)
# set_example4.remove(7)  # This will raise an error


# Discard an element
set_example4.discard(6)
print(set_example4)
# set_example4.discard(6)  # No problem. The set remains unchanged


# Pop an item
popped_element = set_example4.pop()  # No guarantee which element will be popped since set is unordered
print(popped_element)
print(set_example4)


# Union of two sets
set_example5 = {1, 2, 3}
set_example6 = {3, 4, 5}
union_set = set_example5.union(set_example6)
print(union_set)  


# Intersection of two sets
set_example7 = {1, 2, 3}
set_example8 = {3, 4, 5}
intersection_set = set_example7.intersection(set_example8)
print(intersection_set) 


# Difference of two sets
set_example9 = {1, 2, 3}
set_example10 = {3, 4, 5}
difference_set = set_example9.difference(set_example10)  # set_example9 - set_example10
print(difference_set) 