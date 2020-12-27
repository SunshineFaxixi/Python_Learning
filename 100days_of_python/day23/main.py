from turtle import Screen
import time

from player import Player
from car_management import CarManager
from score_board import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()


player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect finish to the top line
    if player.is_finish():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

screen.exitonclick()