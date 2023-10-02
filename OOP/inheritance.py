class Vechine:
    def __init__(self, brand, year) -> None:
        self.brand = brand
        self.year = year

    def drive(self):
        print("the vechine is in mootion")

    def stop(self):
        print("The vechine has stopped")


class Car(Vechine):
    def __init__(self, brand, year, fuel_type) -> None:
        super().__init__(brand, year)
        self.fuel_type = fuel_type
    def drive(self):
        print("The car s driving on the road")


class Bicycle(Vechine):
    def __init__(self, brand, year, vechine_color ) -> None:
        super().__init__(brand, year)
        self.vechine_color = vechine_color
    
    def stop_bicycle(self):
        print("The bicycle has stopped")

    def driving(self):
        print("The bicycle is in mootion")


car1 = Car("Toyota", 2021, "Petrol")
bicycle = Bicycle("Ukraina", 2005, "blue")
bicycle.stop_bicycle
bicycle.driving


