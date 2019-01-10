
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
        self.pay = int(self.pay * self.raise_amount)

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

############################################### Inheritance Creating Subclasses ####################################

class Developer(Employee):
    raise_amount = 1.10
    num_employees = 0

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

        Developer.num_employees += 1

dev_1 = Developer('gilfoyle', 'rocks', 50000, 'Python')
dev_2 = Developer('peter', 'hendricks', 40000, 'Javascript')

print(dev_1.__dict__)
dev_1.apply_raise()
print(dev_1.pay)
print('Number of Employees: '+ str(Employee.num_employees))
print('Number of Developers: ' + str(Developer.num_employees))

####################################### Manager ###########################################
class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

        Developer.num_employees += 1

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print(emp.fullname() + ' removed')

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())


mgr_1 = Manager('Sue','Smith',90000,[dev_1])
print()
print("############### MANAGER ################")
print(mgr_1.email)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
mgr_1.add_emp(dev_1)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print('########################### some other things #####################################')
print(isinstance(mgr_1, Manager),isinstance(dev_2, Manager), isinstance(mgr_1, Employee))
print(issubclass(Manager, Employee), issubclass(Manager, Developer))

class Tech(Developer):
    pass
print(issubclass(Tech, Employee))