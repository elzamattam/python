'''
Given two lists, find missing elements in the second list compared to the first 
Note: Elements in the lists will be unique
Example: -
Input: [2,3,6,1,4], [2,3,1]
Output: [6,4] or [4,6]
'''

# List Time Complexity: O(n1 * n2);  Set Time Complexity: O(n1 + n2) -> So using set
def find_missing_elements(list1: list, list2: list) -> list:
    '''Finds missing elements in list2 as compared to list1'''
    
    result_list = list(set(list1).difference(set(list2)))  # result_list = list(set(list1) - set(list2))
    return result_list


result = find_missing_elements([1,2,3,5],[2,3,6,7])
print(f"Missing elements in the List 2 are: {result}")

result = find_missing_elements([1,2,3,5],[2,3,6,7,8,9,44])
print(f"Missing elements in the List 2 are: {result}")

result = find_missing_elements([1, 2], [1, 2, 3, 5])
print(f"Missing elements in the List 2 are: {result}")

































def find_missing_element(full_list: list, partial_list: list):
    set_full = set(full_list)
    set_partial = set(partial_list)

    missing_elements = list(set(full_list) - set(partial_list))
    return missing_elements


print(find_missing_element([2,3,6,1,4], [2,3,1]))