'''
The python __init__ method is declared within a class and is used to initialize the attributes of an object as soon as the object is formed. While giving the definition for an __init__(self) method, a default parameter, named 'self' is always passed in its argument. This self represents the object of the class itself.

'''

class Employee :
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    
    def getSalary(self):
        print(self.salary)

'''
rohan = Employee("Rohan" , "987987")
print(rohan.salary, rohan.name)
rohan.getSalary()

Ann = Employee("Ann" , "787")
print(Ann.salary, Ann.name)
Ann.getSalary()

'''
