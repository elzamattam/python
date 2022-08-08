def divide(dividend: int, divisor: int) -> float:
    # if divisor == 0:
    #     raise ZeroDivisionError('What have you done! You should not divide a number by zero')

    result = dividend / divisor
    return result


def getShortHandOfDirection(direction: str) -> str:
    '''This function returns the short hand ('l' or 'r' or 'u' or 'd') of given direction.
       If input is not a direction, a ValueError exception would be raised'''

    if direction == 'left':
        return 'l'
    elif direction == 'right':
        return 'r'
    elif direction == 'up':
        return 'u'
    elif direction == 'down':
        return 'd'
    else:
        # Input string is not a direction. This is abnormal.
        raise ValueError('The input is not a direction!')
        

# try:
#     res = divide(10, 0)
#     print(f'Success. Got Result: {res}')
# except ZeroDivisionError as err:
#     print(f'Got zero division error. Error: {err}')
# except Exception as err:
#     print(f'Got unknown error: {err}')
# finally:
#     print('Program executed.')


def executeBiggerLogic():
    try:
        print(getShortHandOfDirection('abc'))
    except ValueError as err:
        print(f'Got a value error: {err}')
    except Exception as err:
        print(f'Got unknown error: {err}')
        raise  # Raise to the caller
    finally:
        print('Program executed')


executeBiggerLogic()