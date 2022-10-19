from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.nivel()

    def nivel(self):
        self.clear()
        self.goto(-240, 250)
        self.write(f"Nivel: {self.level}", align="center", font=(FONT))

    def level_up(self):
        self.level += 1
        self.nivel()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=(FONT))