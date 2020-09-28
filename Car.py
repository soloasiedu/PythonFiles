import random


class Car:
    numOfCars = 0
    __speed = 0
    numOfSeats = 0

    def __init__(self, model, year, horsepower):
        self.model = model
        self.year = year
        self.horsepower = horsepower
        Car.numOfSeats = 4
        Car.numOfCars += 1
        Car.__speed = random.randint(300, 500)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_horsepower(self):
        return self.horsepower

    def get_speed(self):
        return Car.__speed

    def __del__(self):
        print('Car removed')
        Car.numOfCars -= 1

    def __str__(self):
        return "This is a car"


car1 = Car('Range Rover', 2019, 500)
car2 = Car('Bugatti', 2020, 1000)
car3 = Car('Picanto', 2007, 85)
del car3
print(str(Car.numOfCars))
print(car2)
