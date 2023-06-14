import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#CREATE THE TURTLE
player = Player()

#MOVE THE TURTLE
screen.listen()
screen.onkey(player.go_up, 'Up')

#CREATE CAR
car = CarManager()

#CREATE THE SCOREBOARD
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()
    scoreboard.show_score()

    #DETECT COLLISION WITH CAR
    for item in car.all_cars:
       if item.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

    #SUCCESS CROSSING
    if player.ycor() > 280:
        player.go_to_starting_position()
        scoreboard.update_score()
        car.increase_speed()



screen.exitonclick()