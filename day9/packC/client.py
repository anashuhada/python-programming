# Approach 1
import sys
sys.path.append("/Users/anashuhada/PycharmProjects/PythonProgramming/day9/packA")
sys.path.append("/Users/anashuhada/PycharmProjects/PythonProgramming/day9/packB")

import employee
emp_obj= employee.Employee(101, "David", 50000)
emp_obj.display_employee()

import student
stud_obj = student.Student(102, "Scott", "A")
stud_obj.display_student()

# Approach 2
import sys
sys.path.append("/Users/anashuhada/PycharmProjects/PythonProgramming/day9/packA")
sys.path.append("/Users/anashuhada/PycharmProjects/PythonProgramming/day9/packB")

from employee import Employee
obj_emp = Employee(101, "David", 50000)
obj_emp.display_employee()

from student import Student
obj_stud = Student(102, "Scott", "A")
obj_stud.display_student()