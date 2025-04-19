class Vehicle:
    def move(self):
        pass  # This will be overridden

class Car(Vehicle):
    def move(self):
        print("The car is driving on Thika Road")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying from JKIA to Eldoret")

class BodaBoda(Vehicle):
    def move(self):
        print("The boda boda is weaving through Nairobi traffic")

# List of vehicle objects
vehicles = [Car(), Plane(), BodaBoda()]

# Loop through and call the move() method
for v in vehicles:
    v.move()
