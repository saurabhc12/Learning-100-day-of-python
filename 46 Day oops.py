class person:
    name = "gaurav"
    occupacation = " software developer"
    networth = 1000
    def info(self):
        print(f"{self.name} is a {self.occupacation}")

a = person()
b = person()
a.name = "Nikhil"
a.occupacation = "jr developer"

b.name = "sakshi"
b.occupacation = "house wife"
a.info()
b.info()



