

class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        
    
    def drive(self):
        print(f"Driving {self.manufacturer} {self.name}")
        print()
        
        
    def turn(self, direction):
        print(f"Turing {self.name} to", direction)
        print()
        
    
    def brake(self):
        print(f"{self.name} is stopping!")
        print()
        

class Car(Vehicle):
    
    def change_gear(self, gear_name):
        print(f"{self.name} is changing gear to", gear_name)

        
if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford", "Read")
    
    c.drive()
    c.brake()
    c.change_gear("PP")
    
    # v1 = Vehicle("Fusion 110 EX", "Walton", "Black")
    # v2 = Vehicle("Softail Delux", "Harley", "Blue")
    # v3 = Vehicle("Mustang 332 EX", "anoor", "read")
    
    # v1.drive()
    # v2.drive()
    # v3.drive()
    
    # v1.turn("left")
    # v2.turn("Right")
    
    # v1.brake()
    # v2.brake()
    # v3.brake()