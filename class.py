
# Decleration of class
class Person:
    def __init__(self,name,dob,ht):
        #self is look this in java language
        #every internal method has self parameter
        self.name=name
        self.date_of_birth=dob
        self.height=ht
    def getData(self):
        return f"Name: {self.name},DOB: {self.date_of_birth},Height: {self.height}"


obj=Person("Hadiuzzaman","1998","5.5 feet")
val=obj.getData()
print(val)

# make private variable using __ keyword

class Man:
    def __init__(self ,name,age,mobile):
        self.name=name # by default public member
        self.__age=age # make as private using __
        self.__mobile=mobile # make as private

    def getAge(self):
        return self.__age


hadi=Man('hadiuzzaman',24,'01785304677')
print(hadi.name) # access directly because it's a public variable
print(hadi.age) # can not access because it's a private variable,if
#we access this variable we need priviously decleretive method which can
#return those...
print(hadi.getAge()) # that's working great

