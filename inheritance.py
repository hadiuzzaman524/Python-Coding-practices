class Person:
    def __init__(self,person_name:str,year_of_birth:int,height:int):
        self.__name=person_name
        self.__date_of_birth=year_of_birth
        self.__height=height
        self.abc=None

    def get_year_of_birth(self):
        return self.__date_of_birth
    def get_name(self):
        return self.__name
    def set_name(self,newName):
        self.__name=newName

    def get_summery(self):
        print("Method in Person class:")
        return f"name:{self.__name} DOB: {self.__date_of_birth} Height: {self.__height}"


class Student(Person):
    def __init__(self, person_name: str, year_of_birth: int, height: int,email:str,student_id:str):
        super().__init__(person_name, year_of_birth, height)
        self.id=student_id
        self.email=email

    #overriden method.....
    def get_summery(self):
        print("Method in Student class:")
        return f"name:{self.get_name()} Email: {self.email} Year: {self.get_year_of_birth()}"

    # direct print object values
    def __str__(self):
        #return self.get_summery()
        return f"name:{self.get_name()} Email: {self.email} Year: {self.get_year_of_birth()}"

    # this overridden method also help us debugging the code........
    #def __repr__(self):
        #return f"name:{self.get_name()} Email: {self.email} Year: {self.get_year_of_birth()}"

student=Student("hadi",2020,55,"hadiuzzaman@gmail.com","1702020")
print(student.get_summery())
print(student) # use __str__(self): method for printing direct object value.
# every python class have __str__ overridden method


# use class like structure

class Book:
    pass
# in python structure any time create new property
obj=Book
obj.name="Java"
obj.price="230"
obj.author="Hadi"

print(obj.author)