''' 
Remove duplicates from a list
Example: -
Input: [1, 2, 2, 1, 3]
Output: [1, 2, 3]
'''


import time


def remove_duplicates_using_set(duplicates_list:list) -> list:
    '''Removes duplicates using set; order will not be maintained'''
    # Time complexity: O(n); i.e. has an order of magnitude of 'n'
    return list(set(duplicates_list))


def remove_duplicates_using_list(duplicates_list: list) -> list:
    '''Removes duplicates using set; order will be maintained'''
    # Time complexity: O(n**2); i.e. has an order of magnitude of 'n squared (means this is much slower than the set method)'
    non_duplicates_list = []
    for item in duplicates_list:
        if item not in non_duplicates_list:
            non_duplicates_list.append(item)
    return non_duplicates_list


duplicates_list = list(range(10000))  # This is to test time of each function; give a custom list to test the working

start_time = time.time()
non_duplicates_list = remove_duplicates_using_list(duplicates_list)
end_time = time.time()
print(f'Elapsed time: {(end_time - start_time) * 1000} ms')
print(non_duplicates_list)


start = time.time()
non_duplicates_list = remove_duplicates_using_set(duplicates_list)
end_time = time.time()
print(f'Elapsed time: {(end_time - start_time) * 1000} ms')
print(non_duplicates_list)
