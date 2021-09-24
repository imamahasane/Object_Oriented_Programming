def funct(a, b):
    print("It is a Function")
    print(f"{a} and {b}")

class Parson():
    def __init__(self, parson_name, DOB, HT, PN):
        self.name = parson_name
        self.deat_of_birtht = DOB
        self.hight = HT
        self.PhoneNumber = PN

    def set_name(self, new_name):
        self.name = new_name

    def get_summry(self):
        return f"Name: {self.name} \nBirthday: {self.deat_of_birtht} \nHight: {self.hight} \nNumber: {self.PhoneNumber}"



funct(44, 65)

a = Parson("Imam", "12-5-2020", "5.11\"", "01710206224")
print(a.get_summry())

a.set_name("Samilu")
print(a.get_summry())
