class Person:                                                                        # parent class
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place

    def say(self):                                          # must give className parameter......e.g..self
        print(f"{self.name} is {self.age} years old and lives in {self.place}")

class Student(Person):                                                               # Child / Derived class
    pass

# object
std_obj = Student("tanvir",22,"Bangladesh")
std_obj.say()

# print(help(std_obj))            # object detail
