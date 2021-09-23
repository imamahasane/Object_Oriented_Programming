class Car:
    
    def __init__(self, n=None, c=None):
    # def __init__(self, n, c):
        self.name = n
        self.color = c
            
    def start(self):
        print(f"name: {self.name}")
        print(f"Color: {self.color}")
        print("Starting the engine")
        
                    
# my_car = Car("Corolla", "White")
# my_car.start()

for i in range(2):
    name = input()
    color = input()
    # my_car = "mycar"+ str(i)
    # print(my_car)
    mycar = Car(name, color)
    mycar.start()

    
# my_car1 = Car(None, None)
# my_car1 = Car()
# my_car1.name = "Toyota"
# my_car1.color = "Black"

# my_car.start()
# my_car1.start()

# Car.start(my_car)

