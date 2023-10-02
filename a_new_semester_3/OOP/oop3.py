class Animal:
    def walk(self):
        print("I can walk")

    def eat(self):
        print("I can eat")

    
class Dog(Animal):
    def bite(self):
        print("Woof woof")

class Cat(Animal):
    def play(self):
        print("I can paly with my tail")

murka = Cat()

haski = Dog()

murka.walk()