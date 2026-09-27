# Create student class that takes name and marks of 3 subjects as arguments in constructor.
# Then Create methods to calculate average marks.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks  

    def average(self):
        sum=0
        for mark in self.marks:
            sum+=mark
        print("Average marks of",self.name,"is",sum/3)


s1=Student("John",[85,90,78])
s1.average()