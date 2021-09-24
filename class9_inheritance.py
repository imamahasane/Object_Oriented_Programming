
class Vehicle:
    
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        
    
    def drive(self):
        print(f"Driving {self.manufacturer} {self.name}")
        
    
    def turn(self, direction):
        print(f"Turning {self.name} to", direction)
        
        
    def brake(self):
        print(f"{self.name} is stopping!")
        

class Car(Vehicle):
    
    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = 2017
        self.wheels = 4
        
        Car.drive(self)
        
        print(f"A new car has been created. Name: {self.name}")
        print(f"It has {self.wheels} wheels")
        print(f"The car was built in {self.year}")
        
        
if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe" , "Ford", "Red", 2017)