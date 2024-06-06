# Inheritance allow us to define a class that inherits all the method and properties
#form another class

#parent class in the class beging inherites from also colled base class

# child class in the class the inheritance from also colled derived class

class Employee:

    def __init__(self, name,id):
        self.name = name
        self.id=id
    def showDetails(self):
        print(f"the name of the employee : {self.id} is {self.name}")
class programmer(Employee):
    def showLanguages(self):
        print("the default language is python")

e=Employee("xyz",'25')
e.showDetails()
e2 = programmer("Gaurav",50000)
e2.showDetails()
e2.showLanguages()
# e2=Employee("abc",'23')
# print("Empl(oyee Details:"),
#
# print("Name:",e1.name,"age:",e1.age),
# print("Name:",e2.name,"age:",e2.age)

