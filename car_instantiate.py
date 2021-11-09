class Car:
    name = ''
    color = ''
    
    def start(self):
        print("Starting the engine")
        
my_car = Car()

my_car.name = "Lamber Gani"
my_car.color = "Black"

print("The name of car:", my_car.name)
print("Color of the car:", my_car.color)

my_car.start()