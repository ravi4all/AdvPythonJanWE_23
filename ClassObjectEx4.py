class Employee:

    # magic methods
    # constructor - used to initialize variables
    def __init__(self, id, name, salary, dept, designation):
        self.id = id
        self.name = name
        self.salary = salary
        self.dept = dept
        self.designation = designation

    def showDetails(self):
        print("ID :", self.id)
        print("Name :", self.name)
        print("Salary :", self.salary)
        print("Department :", self.dept)
        print("Designation :", self.designation)


emp_1 = Employee(101, "Ram", 56000, "IT", "Developer")
emp_1.showDetails()

emp_2 = Employee(102, "Shyam", 45000, "IT", "Tester")
emp_2.showDetails()

