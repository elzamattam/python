
# Defining the 'find_sum' function
def find_sum(number1: int, number2: int) -> int:
    result = number1 + number2  # Local: This has only scope inside 'find_sum'
    return result

result = 0  # Global; This has nothing to do with 'result' inside 'find_sum"
print(result)  # Prints 0

sum = find_sum(2, 3)  # Calling the 'find_sum' function
print(f'Sum: {sum}. Square of sum: {sum ** 2}')