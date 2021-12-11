class EmployeeName:

    def __init__(self, firstname, lastname, increment):
        self.fullName = firstname + " " + lastname
        self.increment = increment

    # These are instance variables. (Unique to every instance)
    # These are started with self

    def fullName(self):
        # self.fullName = firstname + " " + lastname
        return "self.fullName"

    def calculateIncrement(self):
        self.increment = self.increment * 1.5


employee1 = EmployeeName("Firstname", "LastName createdByConstructor", 500)
print(EmployeeName.fullName(employee1))
# When we are directly running from the class, since this class has a constructor, we have to pass the instance as an arg

print(employee1.increment)
employee1.calculateIncrement()
print(employee1.increment)
