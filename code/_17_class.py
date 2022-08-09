print('Student Details')

# first_student_id = 1
# first_student_name = 'Anu'
# first_student_status = 'Passed'
# print('Details of student1')
# print(f'Id :{first_student_id},Name :{first_student_name}, Status: {first_student_status}')
# second_student_id = 2
# second_student_name = 'Binu'
# second_student_status = 'Passed'
# print('Details of student2')
# print(f'Id :{second_student_id},Name :{second_student_name}, Status: {second_student_status}')

# third_student_id = 3
# third_student_name = 'Elza'
# third_student_status = 'Passed'
# print('Details of student3')
# print(f'Id :{third_student_id},Name :{third_student_name}, Status: {third_student_status}')


class Student:
    def __init__(self, id: int, name: str, status: str):
        self.id = id
        self.name = name
        self.status = status

    def print_details(self) -> None: 
        print(f'Id :{self.id},\nName :{self.name},\nStatus: {self.status}')

    def has_passed(self) -> bool:
        if self.status=='Passed':
            return True
        return False

s1 = Student(1, 'Anu', 'passed')
s1.print_details()
print(s1.has_passed())

s2 = Student(2, 'Binu', 'Failed')
s2.print_details()
print(s2.has_passed())

s3 = Student(3, 'Ram', 'Pending')
s3.print_details()
print(s3.has_passed())

s4 = Student(4, 'Divya', 'Passed')
s4.print_details()
print(s4.has_passed())