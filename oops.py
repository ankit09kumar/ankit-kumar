class Student:
    name = "karan"
    def  __init__(self , fullname):
        self.name = fullname
        print("adding new student in database..")
    
s1 = Student("karan")
print(s1.name)

s2 = Student("arjun")
print(s2.name)