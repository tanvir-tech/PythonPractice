class Student:                                                  # class
    class_variable_1 = 20
    def __init__(self,name,age):                                # constructor function
        self.name = name
        self.age = age
                                      # class variable

    def say(self):                                              # method defination
        print(f"{self.name} is {self.age} years old")

std_obj = Student("tanvir",22)                                  # object creation
std_obj.say()                                                   # method call

#del std_obj.name                                                # deleting object property
#print(std_obj.name)
#del std_obj                                                    # deleting object
print(std_obj)

print(std_obj.__dict__)                                        # properties to a dictionary
print(Student.__dict__)                                        # class to a dictionary
