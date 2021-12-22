class employee:
    increment = 1.5;

    def __init__(self, firstname, lastname, salary):
        self.fullName = firstname + " " + lastname
        self.salary = salary

    # These are instance variables. (Unique to every instance)
    # These are started with self

    def fullName(self):
        # self.fullName = firstname + " " + lastname
        return "self.fullName"

    def calculateIncrement(self):
        self.increment = self.increment * 1.5

    def raiseAmount(self):
        self.salary = int(self.salary * self.increment)  # Casting to return as an integer


employee1 = employee("Kasun", "Nirmala", 20000)
print(employee1.salary)
employee1.raiseAmount()
print(employee1.salary)

# Class methods - affects all instance of the class

