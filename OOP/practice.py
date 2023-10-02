"""class Cat:
    def __init__(self,name, age):
        self.name: str = name
        self.age: int = age

    def get_info(self):
        print(f"Name: {self.name}. Age: {self.age}")

    def __str__(self):
        return f"Cat - {self.name}"
    
cat1 = Cat("Major", 2)
#print(cat1.__dict__)
cat1.get_info()

#print(cat1)

###########
class Student:
    def __init__(self,name,course):
        self.name = name
        self.course = course
        self.subjects =[]

    def add_new_subject(self, new_subject):
        self.subjects.append(new_subject)

s1 = Student("Yarslav", 1)
s1.add_new_subject("Math")
#print(s1.subjects)
   #####################


class Book:
    def __init__(self,name, autor, year):
        self.name = name
        self.autor = autor
        self.year = year
    
    def __str__(self):
        return f"Book - {self.name} autor - {self.autor}, year - {self.year}"

b1 = Book("Robinson Crussoe", "Daniel Defoe", 1837)
print(b1)
"""

