
# Create an empty list
empty_list = []
print(empty_list)


# Convert range to list
range_of_numbers = list(range(1, 101))
print(range_of_numbers)


# Accessing list elements
items = [1, 2, 3, 4, "apple", True]  # Different datatypes possible within list
print(items[4])  # Print an element of using index
print(len(items))  # Print length of list


# Combine 'items1' and 'items2'
items1 = [1, 2, 2]
items2 = [3, 4]
items_combined = items1 + items2  
print(items_combined)


# Add 'items2' to 'items1'
items1 = [1, 2, 2]
items2 = [3, 4]
items1.extend(items2)  
print(items1)


# Append 1 element to the end of 'items_combined' list
items_combined.append(10)  
print(items_combined)


# Insert element '11' as the 3rd index
items_combined.insert(3, 11)  
print(items_combined)


# Pop the last element and returns it
popped_element = items_combined.pop()  
print(popped_element)


# Pop the element in 3rd index and returns it
popped_element = items_combined.pop(3)  
print(popped_element)


# Remove the first occurence of element 2
items_combined.remove(2)  
print(items_combined)


# List slicing (just like string slicing)
print(items_combined[1:4])


# Reverse the list in-place (i.e. new list is not created; existing one gets modified)
items_combined.reverse()
print(items_combined)


# Sort the list in ascending order in-place
items_combined.sort()
print(items_combined)


# Sort the list in descending order in-place
items_combined.sort(reverse=True)
print(items_combined)


# Program to square every element of the list - using for loop
squared_list = []
for i in items_combined:
    squared_value = i * i
    squared_list.append(squared_value)
print(squared_list)


# Program to square every element of the list - using list comprehension
squared_list = [i * i for i in items_combined]  # list comprehension
print(squared_list)


# Explicitly provide type for the list 'number_list'. Here the list can ONLY have elements of type 'int'
number_list: list[int] = [1, 2]


# List of lists - Accessing elements
list_of_lists = [[1, 2, 3], [4, 5, 6]]
list_of_lists.append([7, 9])
first_list = list_of_lists[0]
print(first_list)
second_element_of_first_list = first_list[1]
print(second_element_of_first_list)
