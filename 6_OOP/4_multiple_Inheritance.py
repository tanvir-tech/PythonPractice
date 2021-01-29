class Male:
    def say(self):
        print("Male")

class Female:
    def say(self):
        print("Female")

class Student(Male,Female):      # Multiple Inheritance (sequence based)
    pass



obj = Student()
obj.say() #male
obj2 = Student()
obj2.say() #male......................................only first class method is inherited


