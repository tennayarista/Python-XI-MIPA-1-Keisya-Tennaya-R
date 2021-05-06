class Person (object):

    #Constructor 
    def __init__(self, name):
        self.name = name 

    #To get name 
    def getName(self):
        return self.name

    #To check if this person is an employee
    def isEmployee(self):
        return False 

#inherited or Subclass (Note Person in bracket)
class Employee(Person):

    #Here we return 
    def isEmployee(self):
        return True 

#Driver code 
emp = Person("Joni") # An object of person 
print(emp.getName(), emp.isEmployee())

emp = Employee("Wawan") #An object of empolyee
print(emp.getName(), emp.isEmployee())

