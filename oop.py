# Create class

class Employee:
   # pass #skip for now
#    num_of_emps = 0
#    raise_amount = 1.04
   def __init__(self, first, last):
       self.first=first
       self.last=last
    #    self.pay=pay
    #    self.email=first + '.' + last + '@company.com'

    #    Employee.num_of_emps+=1

   @property  #decorator
   def email(self):
       return '{}.{}@email.com'.format(self.first, self.last)

   @property
   def fullname(self):
       return ('{} {}'.format(self.first, self.last))

   @fullname.setter
   def fullname(self, name):
       first, last=name.split(' ')
       self.first = first
       self.last = last

   @fullname.deleter
   def fullname(self):
       print('Delete Name!')
       self.first = None
       self.last = None

#    def apply_raise(self):
#        self.pay = int(self.pay*self.raise_amount)

#    def __repr__(self): #changes how objects displayed
#        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)
#    def __str__(self):
#        return '{}-{}'.format(self.fullname(), self.email)
#    def __add__(self, other):
#        return self.pay + other.pay
#    def __len__(self):
#        return len(self.fullname())

#    @classmethod
#    def set_raise_amt(cls, amount):
#        cls.raise_amount = amount
#    @classmethod
#    def from_string(cls, emp_str):
#        first, last, pay=emp_str.split('-')
#        return cls(first, last, pay)
#    @staticmethod
#    def is_workday(day):
#        if day.weekday() == 5 or day.weekday() == 6:
#            return False
#        return True

# class Developer(Employee):
#     raise_amt = 1.10
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang=prog_lang
# class Manager(Employee):
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#     def  add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#     def remove_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.remove(emp)
#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())

# emp_1=Employee('Corey', 'Schafer', 50000)
# emp_2=Employee('Test', 'Employee', 60000)
# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))
# print(emp_1+emp_2)
# print(len(emp_1))
# dev_1=Developer('Corey', 'Schafer', 50000, 'Python')
# dev_2=Developer('Test', 'User', 60000,'JavaScript')

# mgr_1 = Manager('Sue', 'Smith', 90000,[dev_1])

emp_1=Employee('John', 'Smith')

# emp_1.fullname = 'John Smith'
emp_1.fullname='Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
