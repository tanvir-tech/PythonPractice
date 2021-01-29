from abc import ABC,abstractmethod
class Person(ABC):                                                                        # Abstract class
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place

    @abstractmethod
    def say(self):
        pass

class Student(Person):
    def say(self):                                                                      # Abstract method implementation
        print(f"{self.name} is {self.age} years old and lives in {self.place}")


std_obj = Student("tanvir",22,"Bangladesh")
std_obj.say()
