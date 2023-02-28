"""
Class methods and Static methods.
"""


class simple:
    pass


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

    @classmethod  # Used as an dependent function of the class
    def from_string(cls, em_st):
        first, last, pay = em_st.split("-")
        return cls(first, last, pay)

    @staticmethod  # Used as an independent function
    def is_workday(day):
        print(day.weekday())
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("fortune", "young", 50000)
emp_2 = Employee("david", "young", 6000)

import datetime

my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))


# Class method
# st_1 = "Fadare-Praise-900"

# emp_11 = Employee.from_string(st_1)
# print(emp_11.email)

# emp_11.apply_raise()

# print(emp_11.pay)

# print(Employee.num_of_emp)

# emp_1 = Employee("fortune", "young", 50000)
# emp_2 = Employee("david", "young", 6000)

# print(Employee.num_of_emp)

# print(emp_1.email)

# # emp_1.first = "bolu"
# # print(emp_1.pay)
# # print(emp_2.pay)

# Employee.raise_amount = 3
# # emp_2.raise_amount = 0

# emp_1.apply_raise()
# # emp_2.apply_raise()

# print(emp_1.pay)
# # print(emp_2.pay)


# # print(emp_1.fullname())
# # print(Employee.fullname(emp_2))
