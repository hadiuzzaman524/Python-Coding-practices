from typing import List


class Person:
    def __init__(self, name:str,age:int, cgpa:float):
        self.name=name
        self.age=age
        self.cgpa=cgpa

    def getAge(self):
        return self.age

    def getSummary(self):
        return f"{self.name} {self.age} {self.cgpa}"

# list of objects
l=[]
l.append(Person('Hadi',32,3.03))
l.append(Person('Mantasha',22,3.00))
l.append(Person('ashrafi',16,3.02))

for i in l: # here i is Person type object
   if(i.getAge()>25): 
       print(i.getSummary())