class Human:
    def __init__(self, title, hp, stamina, speed, level, attack, reload) -> None:
        self.title = title
        self.hp = hp
        self.stamina = stamina
        self.speed = speed
        self.level = level
        self.attack = attack
        self.reload = reload
        self.last_attack = None

    def __str__(self) -> str:
        return f"Race: {self.title}"

class Archer(Human):
    def __init__(self, level) -> None:
        self.title = "Archer"
        super().__init__(self.title, 80 + level*20, 105 + level*5, level, 45+level*5)
class Wizard(Human):
    def __init__(self, level) -> None:
        self.title = "Archer"
        super().__init__(self.title, 80 + level*20, 105 + level*10, level, 200+level*5)

class Warior(Human):
    def __init__(self, level) -> None:
        self.title = "Archer"
        super().__init__(self.title, 80 + level*20, 130 + level*5, level, 45+level*100)
        