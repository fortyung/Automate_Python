"""
Special methods/ Magic methods.
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

    def __repr__(self):
        return f"Employe('{self.first}', '{self.last}', '{self.pay}')"

    # the __str__ method overrides the __repr__ when: print(emp_1)
    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    def __sub__(self, other):
        return self.pay - other.pay


emp_1 = Employee("fortune", "young", 50000)
emp_2 = Employee("david", "young", 6000)

# print(emp_1)

print(repr(emp_1))
print(str(emp_1))
print(emp_1 + emp_2)

print(len(emp_2))

print(len(emp_2.fullname()))  # to verify

print(emp_1 - emp_2)
