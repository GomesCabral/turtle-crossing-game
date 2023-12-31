from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        #new_y = self.ycor() + 10
        #self.goto(self.xcor(), new_y)
        self.forward(MOVE_DISTANCE)

    def go_to_starting_position(self):
        self.goto(STARTING_POSITION)