from shutil import move
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,5)
        if random_chance == 1:
            self.newcar = Turtle()
            self.newcar.shape("square")
            self.newcar.shapesize(1, 2)
            self.newcar.color(random.choice(COLORS))
            self.newcar.penup()
            self.newcar.goto(300, random.randint(-230,230))
            self.all_cars.append(self.newcar)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def car_reset(self):
        for car in self.all_cars:
            car.hideturtle()
            self.all_cars = []

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT