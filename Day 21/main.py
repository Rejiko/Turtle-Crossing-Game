import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(key="w", fun=player.move_forward)

game_is_on = True
while game_is_on:
    car_manager.move_car()
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            player.player_reset()

    if player.ycor() > 280:
        scoreboard.level_increase()
        player.player_reset()
        car_manager.increase_speed()