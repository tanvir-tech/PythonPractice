from abc import ABC,abstractmethod
class Person(ABC):                                                                        # parent class
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place

    @abstractmethod
    def say(self):                                          # must give className parameter......e.g..self
        pass

class Student(Person):                                                               # Child / Derived class
    def say(self):
        print(f"{self.name} is {self.age} years old and lives in {self.place}")

#object
std_obj = Student("tanvir",22,"Bangladesh")
std_obj.say()

print(help(std_obj))            # object detail