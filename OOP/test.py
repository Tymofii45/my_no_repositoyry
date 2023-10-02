class Person():
    name = ""
    age = 0
    gender = ""

    def say_hello(self):
        print(f"Hello, my name is {self.name}")




person1 = Person
person1.name = "Tima"
person1.age = 16
person1.gender = "Male"

#print(person1.__dict__) -- look throught object files

class Animal():
    name = ""
    age = 0

    def say_hello(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}")

Animal1 = Animal()
Animal1.name = "Teddy"
Animal1.age = 25

Animal1.say_hello()

Animal2 = Animal()
Animal2.name = "Petro"
Animal2.age = 12

Animal2.say_hello()

class Car():
    def __init__(self, brand: str, year: int, max_speed: int):
        self.brand =brand
        self.year = year
        self.max_speed = max_speed
    
    def get_max_speed(self, new_max_speed):
        return self.max_speed
    
    def set_max_speed(self, new_max_speed):
        self.max_speed = new_max_speed

volvo = Car(brand="Volvo", year=2022, max_speed=260)
#print(volvo.get_max_speed())
volvo.set_max_speed(310)
#print(volvo.get_max_speed())
#=============
class BankAkount:
    def __init__(self, owner_name: str, account_id: int, balance: float = 0):
        self.owner = owner_name
        self.account = account_id
        self.balance = balance

    def add_money(self, invoice:float):
        self.balance += invoice
        print(f"You added {invoice} dollars. Your balance: {self.balance} dollars")

    def withdraw(self, money):
        if money > self.balance:
            print("You don't have enought money")
        else:
            self.balance -= money
            print("You succcesfully cashed out {money}")
    
acoount1 = BankAkount("Tymofii", 2234534, 2789)
acoount1.add_money(1000)
acoount1.withdraw(37899)