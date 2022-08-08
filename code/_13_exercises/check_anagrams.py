'''
Check if two strings are anagrams (made of same characters with same frequencies)
Examples: -
Input: danger,garden
Output: True
Input: Name less,salesmen
Output: True
Input: nameles,salesme
Output: False
'''

# Takes O(nlogn) time complexity
def check_if_anagrams_using_sort(string1:str, string2:str) -> bool:
    string1 = string1.replace(' ','').lower()
    string2 = string2.replace(' ','').lower()
  
    if len(string1) != len(string2):
        return False

    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    
    if sorted_string1 == sorted_string2:
        return True

    return False    


# Takes O(n) time complexity
def check_if_anagrams_using_dict(string1:str, string2:str) -> bool:
    string1 = string1.replace(' ','').lower()
    string2 = string2.replace(' ','').lower()
  
    if len(string1) != len(string2):
        return False

    char_counts = {}

    for char in string1: 
        if char in char_counts:
            char_counts[char] = char_counts[char] + 1
        else:
            char_counts[char] = 1

    for char in string2:
        if char in char_counts:
            char_counts[char] = char_counts[char] - 1
        else:
            return False

    for char in char_counts:
        if char_counts[char] != 0:
            return False
    
    return True


# Automated tests; also known as (in development context) - 'Test Driven Development (TDD)' or 'Unit Tests'


test1_sort = check_if_anagrams_using_sort('garden','danger') == True
test2_sort = check_if_anagrams_using_sort('garden','dangerg') == False
test3_sort = check_if_anagrams_using_sort('Garden','danger') == True
test4_sort = check_if_anagrams_using_sort('Ga rden','da  nger') == True


if test1_sort and test2_sort and test3_sort and test4_sort:
    print('All tests using sort passed!!')
else:
    print('Some tests using sort failed..')    


test1_dict = check_if_anagrams_using_dict('garden','danger') == True
test2_dict = check_if_anagrams_using_dict('garden','dangerg') == False
test3_dict = check_if_anagrams_using_dict('Garden','danger') == True
test4_dict = check_if_anagrams_using_dict('Ga rden','da  nger') == True


if test1_dict and test2_dict and test3_dict and test4_dict:
    print('All tests using dict passed!!')
else:
    print('Some tests using dict failed..')    
