
class Employee:

    raise_amount = 1.04
    num_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_holiday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return True
        return False

emp1 = Employee('toha', 'khan', 55000)
emp2 = Employee('asif', 'ahmed', 45000)

emp_str_1 = 'John-Doe-70000'

############ Displaying Methods #############
emp1.raise_amount = 1.05
print(emp1.__dict__)
print(Employee.raise_amount)
Employee.set_raise_amt(1.06)
print(emp1.__dict__)
print(Employee.raise_amount)
############ Displaying Methods #############
print()
emp3 = Employee.from_string(emp_str_1)
print(emp3.__dict__, "Employee Count: " + str(Employee.num_employees))

############## static methods ##########################
import datetime

my_date = datetime.date(2018, 8, 15)
print(Employee.is_holiday(my_date))
