class Employee:
    annualRaise = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str(first[0] + '.' + last + '@company.com').lower()
        
    def fullname(self):
        return '\nNome: {} {}\nemail: {}\n'.format(self.first, self.last, self.email)

emp_1 = Employee('Marcos', 'Manfrin', 50000)
# Employee
emp_2 = Employee('Test', 'User', 40000)
print(emp_1.fullname())
print(Employee.fullname(emp_2))

print(emp_1.annualRaise)
emp_2 = Employee('Test', 'User', 40000)
