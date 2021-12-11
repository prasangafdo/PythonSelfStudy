class Employee:
    incrementRate = 0.1

    def __init__(self, employeeID, employeeName, salary):
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.salary = salary


    def employeeSalaryIncrement(self):
       increment = self.salary* self.incrementRate
       self.salary +=increment
       return self.salary


employee1 = Employee(30021,"Kasun",25000)
Employee.incrementRate = 0.5 #This will impact all the functions
employee1.employeeSalaryIncrement()
print(employee1.salary)

print(Employee.__dict__)
print(employee1.__dict__)

