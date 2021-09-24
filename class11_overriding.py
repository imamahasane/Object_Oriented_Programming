
class Vehicle:
    
    def __init__(self, name, manufacturer, color):
        print("Creating a vehicle")
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        
        
class Car(Vehicle):
    
    def __init__(self, name, manufacturer, color, year):
        print("Create a car.")
        super().__init__(name, manufacturer, color)
        
        self.year = 2017
        self.wheels = 4
        
        
if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford", "Read", 2017)
    print(c.name, c.year, c.wheels)