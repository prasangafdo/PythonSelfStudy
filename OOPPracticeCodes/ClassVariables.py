class Employee:
    incrementRate = 0.1
    employeeCount = 0

    def __init__(self, employeeID, employeeName, salary):
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.salary = salary

        Employee.employeeCount += 1

    def employeeSalaryIncrement(self):
        increment = self.salary * self.incrementRate
        self.salary += increment
        return self.salary


employee1 = Employee(30021, "Kasun", 25000)
Employee.incrementRate = 0.5  # This will impact all the functions
employee1.employeeSalaryIncrement()
print(employee1.salary)

employee2 = Employee(30022, "Dulaj", 25000)
employee2.incrementRate = 0.12  # This will impact only current instance
employee2.employeeSalaryIncrement()
print(employee2.salary)
print(Employee.employeeCount)
# print(Employee.__dict__) # Printing namespaces
# print(employee1.__dict__)
