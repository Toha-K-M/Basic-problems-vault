
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)


emp1 = Employee('toha', 'khan', 55000)
emp2 = Employee('asif', 'ahmed', 45000)

############ Displaying Methods #############
print(emp1.email)
print('{} {}'.format(emp1.first, emp1.last))
print(emp1.fullname())
print(emp2.fullname())
print(Employee.fullname(emp1))
