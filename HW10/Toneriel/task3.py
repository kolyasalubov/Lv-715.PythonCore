# Create an employee class. Each employee has
# characteristics such as name and salary. The class should
# have a counter that calculates the total number of
# employees, as well as a method that prints the total
# number of employees and a method that displays
# information about each employee in particular, namely
# the name and salary.
# In addition to creating a class, display information about
# the base classes from which the employee class is
# inherited (__base__), the class namespace (__dict__),
# the class name (__name__), the module name in which
# the class is defined (__module__), the documentation
# bar ( __doc__)

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
