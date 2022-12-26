#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
#1
class Vehicle:
    name ='Audi X60'
    max_speed = 200
    mileage = 300000

print(Vehicle.name, Vehicle.max_speed)


#2

class Vehicle:
    def velicle_atri(self):
        self.name = 'Audi X60'
        self.max_speed = 200
        self.mileage = 300000
        print(f"Model of car {self.name}  have {self.mileage} mileage and {self.max_speed} max speed")

model = Vehicle()
Vehicle.velicle_atri(model)


