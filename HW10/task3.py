class Employee:
    '''
    Common base class for all employees.
    '''

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def displayCount(self):
        return f"Total Employee {Employee.employee_count}"

    def displayEmployee(self):
        return f"Name : {self.name},  Salary: {self.salary}"


employee_1 = Employee("Gimly", 3500)
employee_2 = Employee("Legolas", 6000)
employee_3 = Employee("Galadriel", 7000)
employee_4 = Employee("Oleksii", 7000)

print(Employee.employee_count)
print(employee_1.displayCount())
print(employee_1.displayEmployee())
print(employee_2.displayEmployee())
print(employee_3.displayEmployee())
print(employee_4.displayEmployee())

print(f"Employee.__doc__:{Employee.__doc__}")
print(f"Employee.__name__:{Employee.__name__}")
print(f"Employee.__module__:{Employee.__module__}")
print(f"Employee.__bases__:{Employee.__bases__}")
print(f"Employee.__dict__:{Employee.__dict__}")