class Employee:
    def takeInput(self, id, name, salary, dept, designation):
        # Local Variable (Accessible only inside takeInput)
        msg = "Taking Input from {}".format(name)
        print(msg)
        
        # Class Level Variable (Accessible throughout the class)
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

emp_1 = Employee()
emp_1.takeInput(101, "Ram", 56000, "IT", "Developer")
emp_1.showDetails()

emp_2 = Employee()
emp_2.takeInput(102, "Shyam", 45000, "IT", "Tester")
emp_2.showDetails()

