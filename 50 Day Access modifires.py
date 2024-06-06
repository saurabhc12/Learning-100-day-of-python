#Most programming languages has three forms of access modifiers, which are Public, Protected and Private in a class.
#Python uses '_' symbol to determine the access control for a specific data member or a member function of a class.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#private

class business:
    def __init__(self):
        self.__name = "gaurav"
a = business()
#print(a.__name)
print(a._business__name)

