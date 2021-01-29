class Person:
    def __init__(self,name):
        self.name=name
        print("Person Constructor")

class Male:
    def __init__(self,age):
        self.age=age
        print("Male Constructor")

class Student(Person,Male):                 # Multiple Inheritance (sequence based)
    def __init__(self,id,name,age):
        Person.__init__(self,name)          # super can't be used for multiple inheritance
        Male.__init__(self,age)
        self.id=id
        print("Student Constructor")


obj = Student(18043,"Tanvir",22)
print("Student id is ",obj.id)




