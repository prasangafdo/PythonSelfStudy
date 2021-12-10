class EmployeeName:

    def __init__(self, firstname, lastname):
        self.fullName = firstname + " " + lastname
# These are instance variables. (Unique to every instance)

    def fullName(self):
        # self.fullName = firstname + " " + lastname
        return "self.fullName"


employee1 = EmployeeName("Firstname", "LastName createdByConstructor")
print(EmployeeName.fullName(employee1))
# When we are directly running from the class, since this class has a constructor, we have to pass the instance as an arg

