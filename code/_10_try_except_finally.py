import _7_loops

numbers = [1, 2, 3]

try:
    _7_loops.print_numbers(numbers)
except IndexError:
    print('Encountered index error. Please make sure that the length of input to print_numbers is greater than 2')
except Exception as err:
    print(f'Encountered an error: {err}')
finally:  # Will be executed regardless of error or not
    print('Performed cleanup activity')

print('Program finished successfully!')