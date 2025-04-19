# Base class
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def show_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass (Inheritance)
class FlyingHero(Superhero):
    def __init__(self, name, power, speed):
        super().__init__(name, power)  # Inherit from Superhero
        self.speed = speed

    # Method override (Polymorphism)
    def show_power(self):
        print(f"{self.name} flies with {self.power} at {self.speed} km/h!")

# Create objects
hero1 = Superhero("Mama Justice", "Truth Beam")
hero2 = FlyingHero("Captain Nairobi", "Wind Power", 500)

# Call methods
hero1.show_power()
hero2.show_power()
