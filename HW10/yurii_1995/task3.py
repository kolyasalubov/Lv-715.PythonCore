# home work 10, task 3

# creating a class Employee with methods
class Employee:
    """This class is for employee objects creation"""
    counter = 0

    def __init__(self, name: str, salary: float):
        Employee.counter += 1
        
        self.name = name
        self.salary = salary

    def __str__() -> str:
        print(f"The total number of employees in this class is: {Employee.counter}")

    def show_employee_info(self):
        """This method shows the information details about employee object in console"""
        print(f"The name of your employee is {self.name}")
        print(f"The sum of salary of your employee is {self.salary}")

# example of using the class Employee
employee = Employee("Yurii", 3000.0)
employee2 = Employee("Nazar", 3000.0)
Employee.__str__()
employee.show_employee_info()
employee2.show_employee_info()

# using __mro__ inherited information
print(Employee.__mro__)

# using the base classes from which the employee class is inherited (__base__)
print(Employee.__base__)

# using the class name (__name__)
print(Employee.__name__)

# using the documentation bar ( __doc__)
print(Employee.__doc__)

# using the module name in which the class is defined (__module__)
print(Employee.__module__)

# using the class namespace (__dict__)
print(Employee.__dict__)
