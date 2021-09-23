
class Car:
    
    def __init__(self, n, c):
        self.name = n
        self.color = c
        
    
    def start(self):
        print(f"name: {self.name}")
        print(f"Color: {self.color}")
        print("Starting the engine")
        
        
my_car = Car("Corolla", "White")

Car.start(my_car)