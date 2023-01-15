class Employee:
    """
    This is employee class
    """
    id = None
    name = None
    salary = None
    dept = None

# creating object of Employee class
emp_1 = Employee()
# print(emp_1)
emp_1.id = 101
emp_1.name = "Ram"
emp_1.salary = 45000
emp_1.dept = "IT"
emp_1.designation = "Developer"

# print("ID :",emp_1.id)
# print("Name :",emp_1.name)
# print("Salary :",emp_1.salary)
# print("Department :",emp_1.dept)
# print("Designation :",emp_1.designation)

print(emp_1.__class__, emp_1.__doc__, emp_1.__dict__)
