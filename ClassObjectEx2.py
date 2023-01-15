# SOLID
# DRY - Donot Repeat Yourself

class Employee:
    """
    This is employee class
    """
    id = None
    name = None
    salary = None
    dept = None
    designation = None

    def showDetails(self):
        print("ID :", self.id)
        print("Name :", self.name)
        print("Salary :", self.salary)
        print("Department :", self.dept)
        print("Designation :", self.designation)

emp_1 = Employee()
emp_1.id = 101
emp_1.name = "Ram"
emp_1.salary = 45000
emp_1.dept = "IT"
emp_1.designation = "Developer"

emp_1.showDetails()

# print("ID :",emp_1.id)
# print("Name :",emp_1.name)
# print("Salary :",emp_1.salary)
# print("Department :",emp_1.dept)
# print("Designation :",emp_1.designation)

emp_2 = Employee()
emp_2.id = 102
emp_2.name = "Shyam"
emp_2.salary = 50000
emp_2.dept = "IT"
# emp_2.designation = "Developer"

emp_2.showDetails()

# print("ID :",emp_2.id)
# print("Name :",emp_2.name)
# print("Salary :",emp_2.salary)
# print("Department :",emp_2.dept)
# print("Designation :",emp_2.designation)
