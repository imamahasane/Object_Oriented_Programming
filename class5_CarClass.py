
class Car:
    
    def __init__(self, n, m, c, y, cc):
        self.name = n
        self.manufacturer = m
        self.color = c
        self.year = y
        self.cc = cc
        
        
    def start(self):
        print(f"name: {self.name}")
        print("Starting the engine")
        print()
        return
    
    
    def brake(self):
        print(f"manufacturer: {self.manufacturer}")
        print("manufacturer the engine")
        print()
        Car.start(self)
        return
    
    
    def drive(self):
        print(f"color: {self.color}")
        print("color the engine")
        print()
        Car.brake(self)
        return
    
    
    def turn(self):
        print(f"year: {self.year}")
        print("year the engine")
        print()
        Car.drive(self)
        return
    
    
    def change_gear(self):
        print(f"cc: {self.cc}")
        print("cc the engine")
        print()
        Car.turn(self)
        return
      
    
my_car = Car("Corolla", "ami", "White", "2998", "1620")
my_car.change_gear()

