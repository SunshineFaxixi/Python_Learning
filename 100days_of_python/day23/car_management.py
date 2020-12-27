from turtle import Turtle
import random

COLORS = ["yellow", "blue", "red", "green", "purple"]
MOVE_PACE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = MOVE_PACE

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT

