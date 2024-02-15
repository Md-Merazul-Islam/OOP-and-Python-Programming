"""
Getter: A getter is called when the attribute value is requested for display. This method is called a getter method.

Setter: When a value is set, a function is called. This method is called a setter.
"""


# example:
class Person:
    def __init__(self, Name, Age, roll, village) -> None:
        self.name = Name
        self.age = Age
        self.roll = roll
        self.village = village
    # getter

    @property
    def Get_Name_Age(self):
        return f'Name is : {self.name} and his/her age : {self.age} . His roll is : {self.roll}. His village name is : {self.village}'
    
    # setter
    @Get_Name_Age.setter
    def Set_Name_Age(self, name_age):
         self.age, self.roll, self.village = name_age
        # self.age = age
        # return f'New name : {self.name} and new age : {self.age}'


person = Person("Sakib", 38,1,"Dhaladia")
# getter -> when we use @property then we no need () penrthesis 
print(person.Get_Name_Age)


person.Set_Name_Age = ( 40,2,"Charpar")
print(person.Get_Name_Age)
