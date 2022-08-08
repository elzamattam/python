'''This has some functions to show how loops in Python works'''

def find_sum_using_for_loop(numbers: list[int]):
    # Sum calculation using for loop 
    sum = 0
    for number in numbers:
        sum += number  # sum = sum + number
    print('Sum using for loop: ' + str(sum))


def print_numbers(numbers: list[int]):
    '''Print all numbers using indices. Do not give a list which has greater than 3 elements'''
    print('Priting all numbers using indices:')
    print(numbers[0])
    print(numbers[1])
    print(numbers[2])
    # print(numbers[3])  # Will not work if numbers list length is greater than 3; Best method is to use a loop with 'len' function


def find_sum_using_while_loop(numbers: list[int]):
    # Finding length of 'numbers' using 'len' function
    length_of_numbers = len(numbers)

    # Sum calculation using while loop
    sum = 0
    index = 0
    while index < length_of_numbers:  
        sum = sum + numbers[index]
        index = index + 1
        
    return sum


def find_number_from_list(numbers: list[int], number_to_be_found: int):
    # Loop altering statements - 'break'
    for number in numbers:
        if number == number_to_be_found:
            print(f'Found the number {number_to_be_found}!')
            break  # Break the 'for' loop if this condition is satisfied


def print_and_stop_if_greater_than_number_in_list(numbers: list[int], stopping_number: int):
    # Loop altering statements - 'continue'
    for number in numbers:
        if number > stopping_number:
            continue  # Stop and continue to next iteration of the loop - this means next code statements will not be executed
        print('Printing the number')
        print(number)


# numbers = [1, 2, 3]

# find_sum_using_for_loop(numbers)  # Already has print statements inside it
# print('\n\n')

# print_numbers(numbers)  # Already has print statements inside it
# print('\n\n')

# find_number_from_list(numbers, 2)  # Already has print statements inside it
# print('\n\n')

# print_and_stop_if_greater_than_number_in_list(numbers, 1)  # Already has print statements inside it

# result = find_sum_using_while_loop(numbers)
# print(f'\n\nSum using while loop: {result}')  # print(f'\n\nSum using while loop: {find_sum_using_while_loop(numbers)}')