from _18_enum import StudentStatus


print('\nStudent Details\n---------------\n')


# Without using class

# first_student_id = 1
# first_student_name = 'Anu'
# first_student_status = 'Passed'
# print('Details of student1')
# print(f'Id :{first_student_id}, Name :{first_student_name}, Status: {first_student_status}')

# second_student_id = 2
# second_student_name = 'Binu'
# second_student_status = 'Passed'
# print('Details of student2')
# print(f'Id :{second_student_id}, Name :{second_student_name}, Status: {second_student_status}')

# third_student_id = 3
# third_student_name = 'Elza'
# third_student_status = 'Passed'
# print('Details of student3')
# print(f'Id :{third_student_id}, Name :{third_student_name}, Status: {third_student_status}')


# Using class

class Student:
    def __init__(self, id: int, name: str, status: StudentStatus):
        self.id = id
        self.name = name
        self.status = status

    def print_details(self) -> None: 
        print(f'Id :{self.id},\nName :{self.name},\nStatus: {self.status}')

    def has_passed(self) -> bool:
        if self.status==StudentStatus.Passed:
            return True
        return False


s1 = Student(1, 'Anu', StudentStatus.Passed)
s1.print_details()
print(s1.has_passed())

s2 = Student(2, 'Binu', StudentStatus.Failed)
s2.print_details()
print(s2.has_passed())

s3 = Student(3, 'Ram', StudentStatus.Pending)
s3.print_details()
print(s3.has_passed())

s4 = Student(4, 'Divya', StudentStatus.Passed)
s4.print_details()
print(s4.has_passed())

# Note: If 'status' were a string, user of 'Student' class can instantiate it with invalid strings (i.e. other than 'Passed', 'Failed,' 'Pending')
# So enum was best suited for 'status' and therefore we created and used 'StudentStatus' enum