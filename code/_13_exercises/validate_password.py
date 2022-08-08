'''
Validate a password string with conditions:
	a) Min. 7 letters
	b) At least 1 lower case
	c) At least 1 upper case
	d) At least 1 digit
Example: -
Input: abcd
Output: False
Input: abcD123
Output: True
'''


def validate_password(password: str) -> bool:
    # Checking whether password has min 7 letters
    if len(password) < 7:
        return False

    # Checking whether lowercase, uppercase digit are present in password
    lowercase_present = False
    uppercase_present = False
    digit_present = False
    for letter in password:
        if not lowercase_present:
            lowercase_present = letter.islower()
        if not uppercase_present:
            uppercase_present = letter.isupper()
        if not digit_present:
            digit_present = letter.isdigit()

    return lowercase_present and uppercase_present and digit_present


# Automated tests for the 'validate_password'; also known as (in development context) - 'Test Driven Development (TDD)' or 'Unit Tests'


test1 = validate_password('abcd') == False
test2 = validate_password('abcd123') == False
test3 = validate_password('Abcd12') == False
test4 = validate_password('Abcd123') == True
test5 = validate_password('') == False
test6 = validate_password('bcdefgD12') == True

if test1 and test2 and test3 and test4 and test5 and test6:
    print("All tests passed!!")
else:
    print("Some tests failed!!")
