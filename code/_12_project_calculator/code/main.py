
from cmath import isnan
import calculator_math


def start_calculator():
    while True:
        show_title()

        show_operations()

        operator = get_operator()

        operand1 = get_operand()
        if isnan(operand1):  # 'isnan' is an inbuilt Python function which checks if a number is 'nan'
            print("First operand input was invalid. Stopping calculator.")
            return

        operand2 = get_operand()
        if isnan(operand2):
            print("Second operand input was invalid. Stopping calculator.")
            return

        if operator == '4' and operand2 == 0:
            print('The divisor is 0 for division operation. Stopping calculator.')
            return

        try:
            result = calculate(operator, operand1, operand2)
        except Exception as err:
            print(f'Encountered a problem. Error: {err} Stopping calculator.')
            return

        print(f'Result: {result}')

        while True:
            continue_or_not = input('Do you want to continue (y/n)? ')

            if continue_or_not == 'y' or continue_or_not == 'Y':  # if continue_or_not.upper() == 'Y'
                print('You chose to continue the program. The program will now continue.')
                break
            elif continue_or_not == 'n' or continue_or_not == 'N':  # if continue_or_not.upper() == 'N'
                print('You chose not to continue. The program will exit now.')
                return
            else:
                print('You did not give a valid input. Please retry.')


def show_title():
    print('\n\nCalculator\n----------\n\n')


def show_operations():
    print('Choose an operator from the following: -\n')
    print('1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Exponentiate\n')


def get_operator() -> str:
    while True:
        operator = input('Please input an operator (number) from the above list: ')
        if operator not in ['1', '2', '3', '4', '5']:
            print('The operator you entered is not valid. Please retry.')
        else:
            break
    
    return operator


def get_operand() -> float:
    operand = None

    # Retry 5 times and exit if the user still has not provided a valid input
    for i in range(5):
        try:
            operand = float(input('Please input the operand: '))
            break
        except ValueError:
            print('Encountered an error while retrieving operand. Entered input is not a valid number. Please retry')
        except Exception as err:
            print(f'Encountered an error while retrieving operand. Error: {err}. Please retry')
    
    if operand is None:
        return float('nan')  # Return a special float symbol called 'nan' (Not A Number)
    
    return operand


def calculate(operator: str, operand1: float, operand2: float) -> float:
    if operator == '1':
        result = calculator_math.add(operand1, operand2)
    elif operator == '2':
        result = calculator_math.subtract(operand1, operand2)
    elif operator == '3':
        result = calculator_math.multiply(operand1, operand2)
    elif operator == '4':
        result = calculator_math.divide(operand1, operand2)
    elif operator == '5':
        result = calculator_math.exponentiate(operand1, operand2)
    else:
        raise ValueError('Input operator is invalid')
    
    return result


try:
    start_calculator()
except Exception as err:
    print(f'Calculator program encountered an unforeseen error. Error: {err}')
finally:
    print('Calculator program ended!')




































