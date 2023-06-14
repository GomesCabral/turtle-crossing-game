from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.level = 1
        #self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=('Courier', 20, 'bold'))

    def show_score(self):
        self.goto(-290, 270)
        self.write(f"Level: {self.level}", align='left', font=('Courier', 12, 'normal'))

    def update_score(self):
        self.clear()
        self.level += 1