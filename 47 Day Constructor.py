# class person:
#     name = "saurabh"
#     occupacation = " sr developer"
#
#     def info(self):
#         print(f"{self.name} is a {self.occupacation}")
# a = person()
# a.info()

# contructor is automatically call when we call object lets see the given example
# always zero return

# class person:
#     def __int__(self,name,occ):
#         print("hey i am a person")
#         self.name = name
#         self.occ = occ
#     def info(self):
#         print(f"{self.name} is a {self.occ}")
# a = person("harry","dev")
# b = person ("divy", "HR")

# a.info()
# b.info()
# print(a)

# exmple of parameter contrucator

class GeekforGeeks:

	# default constructor
	def __init__(self):
		self.geek = "GeekforGeeks"

	# a method for printing data members
	def print_Geek(self):
		print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()

#Example of the parameterized constructor :

class Addition:
	first = 0
	second = 0
	answer = 0

	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()

