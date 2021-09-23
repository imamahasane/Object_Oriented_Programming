
class Car:
    name = ''
    color = ''
    
    def start():
        print("Starting the engine.")
        

Car.name = "Axio"
Car.color = "Red"

print(f"Name of the car: {Car.name}")
print(f"Name of the Color: {Car.color}")

Car.start()