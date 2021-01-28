class Person:                                                                        # parent class
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place

    def say(self):                                          # must give className parameter......e.g..self
        print(f"Parent class saying : {self.name} is {self.age} years old and lives in {self.place}")

class Student(Person):                                      # Child / Derived class needs to get more own property
    def __init__(self,name,age,place,course):
        super().__init__(name,age,place)
        self.course = course



# object
std_obj = Student("tanvir",22,"Bangladesh","ICT")
std_obj.say()
print("Student property : ",std_obj.course)


# print(help(std_obj))            # object detail
