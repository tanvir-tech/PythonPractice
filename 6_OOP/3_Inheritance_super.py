class Person:                                               # parent class
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def say(self):
        print(f"Parent Method : {self.name} is {self.age} years old and lives in {self.place}")

class Student(Person):                                      # Child/Derived class
    def __init__(self,name,age,place,course):
        super().__init__(name,age,place)               # super - this is auto called when __init__(child) is not defined
        self.course = course


std_obj = Student("tanvir",22,"Bangladesh","ICT")
std_obj.say()
print("Student property : ",std_obj.course)

