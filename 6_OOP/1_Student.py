class Student:                                               # class
    # name=""                                                  # class variable
    # age=0

    def __init__(self,name,age):                                # constructor
        self.name = name
        self.age = age

    def say(self):                                              # method def.
        print(f"{self.name} is {self.age} years old")


std_obj = Student("tanvir",22)                                  # object creation with constructor
std_obj.say()                                                   # method call by obj.

#del std_obj.name            # deleting object property
#del std_obj                 # deleting object

print(std_obj)

print(std_obj.__dict__)                                        # properties -> dictionary
print(Student.__dict__)                                        # class -> dictionary

# print(help(std_obj))            # object detail