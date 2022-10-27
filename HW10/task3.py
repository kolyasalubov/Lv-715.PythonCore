class Employee:
    COUNT_EMPLOYEE = 0

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        self.__class__.COUNT_EMPLOYEE += 1

    @classmethod
    def count_employees(cls):
        return f"Count of employees = {cls.COUNT_EMPLOYEE}"

    @property
    def get_info(self):
        return f"name: {self.__name}\nsalary: {self.__salary}"


e1 = Employee(name="Vadym", salary=200)
e2 = Employee(name="Vince", salary=200)
print(Employee.count_employees())
print(e1.get_info)
print(e2.get_info)
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
