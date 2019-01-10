
class Employee:

    raise_ammount = 1.04
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
        self.pay = self.pay * self.raise_ammount

emp1 = Employee('toha', 'khan', 55000)
emp2 = Employee('asif', 'ahmed', 45000)

############ Displaying Methods #############
print(emp1.__dict__)
emp1.apply_raise()
print(emp1.pay)
print(Employee.num_employees)

emp1.raise_ammount = 1.05
print(emp1.__dict__)