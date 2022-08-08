input_variable_string = input('Enter a number: ')
input_variable_number = int(input_variable_string)

if input_variable_number < 100:
    print('Entered number is less than 100')
elif input_variable_number == 100:
    print('Entered number is 100')
elif input_variable_number > 100 and input_variable_number < 200:
    print('Entered number is between 100 and 200')
elif input_variable_number == 500 or input_variable_number == 1000:
    print('Entered number is 500 or 1000')
elif input_variable_number > 1000:
    pass  # TODO: need to revisit this condition
else:
    print('Entered number is greater than 200 but not 500 or 1000')

