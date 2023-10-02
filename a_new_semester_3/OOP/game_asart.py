from gameRPG import Archer, Warior, Wizard
from datetime import datetime, timedelta


print("Welcome to the game")
name = input("Enter you name: ")
answer = 0

while answer not in [1, 2, 3]:
    answer = int(input("Chose your role\n 1:Archer  2: Warior  3:Wizard  : "))
    if answer == 1:
        hero = Archer(1)
        hero_name = "Archer"
    elif answer == 2:
        hero = Warior(1)
        hero_name = "Wariror"
    elif answer == 3:
        hero = Wizard(1)
        hero_name = "Wizard"
    else:
        print("Error")

