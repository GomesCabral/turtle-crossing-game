from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        number_cars = random.randint(1, 6)
        if number_cars == 1:
            car = Turtle('square')
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-230, 250)
            #X and Y
            car.goto(300, random_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)