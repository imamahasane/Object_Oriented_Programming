
class Vehicle:
    
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        
        
    def turn(self, direction):
        print(f"Turning {self.name} to", direction)
        print()



class Car(Vehicle):
    
    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = 2017
        self.wheels = 4


    def change_gear(self, gear_name):
            print(f"{self.name} is changing gear to", gear_name)
            
    
    def turn(self, direction):
        print(f"{self.name} is turning to", direction)
        print()


        
if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe" , "Ford", "Red", 2017)
    v = Vehicle("Softail Delux", "noora", 'BLUE')
    
    c.turn("right")
    v.turn("right")
