
class Man:
    def __init__(self,name:str,age:int,gpa:float):
        self.name=name
        self.age=age
        self.__gpa=gpa

    def getInfo(self):
        return f"name: {self.name} Age: {self.age} Gpa: {self.__gpa}"



obj=Man('hadi','42','gfdgfd') # This line of code showing warning because
# we set the parameter list has str,int,float but now we assign all
# argument are str that's why it showing error.....
print(obj.getInfo())


newobj=Man("hadiuzzaman",34,3.75)
print(newobj.getInfo())