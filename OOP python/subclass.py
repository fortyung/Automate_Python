"""
Inheritance and Subclasses.
"""


class Employee:

    num_of_emp = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emp += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 10

    def __init__(self, first, last, pay, prog_lag):
        super().__init__(first, last, pay)
        self.prog_lag = prog_lag


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = employees

        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("fortune", "young", 10, "python")
dev_2 = Employee("david", "young", 20)

mgr_1 = Manager("Dan", "Vin", 8000, [dev_1])

print(isinstance(mgr_1, Employee))
print(issubclass(Manager, Developer))

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)

# mgr_1.print_emp()
# print(mgr_1.email)

# print(dev_1.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print("-------")

# print(dev_2.email)
# print(dev_2.pay)
# dev_2.apply_raise()
# print(dev_2.pay)
