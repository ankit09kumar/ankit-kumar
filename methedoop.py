class Student:
    collage_name = "ABC collagre"
    
    def __init__(self , name , marks):
        self.name  = name
        self.marks = marks
        
    def welcome(self):
        print("welcome student" , self.name)
        
s1  = Student("karan" , 97)
s1.welcome()            