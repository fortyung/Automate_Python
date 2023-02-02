class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + "." + last + "@company.com"

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print("Name deleted!")


emp_1 = Employee("fortune", "young")
emp_2 = Employee("david", "young")

emp_2.fullname = "Sam kinston"

emp_1.first = "youngg"
# print(emp_1.fullname()) # Without property
print(emp_1.fullname)  # With property
print(emp_1.email)

print(emp_2.fullname)

del emp_2.fullname
