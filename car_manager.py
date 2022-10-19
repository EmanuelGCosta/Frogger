from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2


class CarManager():
    def __init__(self):
        super().__init__()
        self.carros = []
        self.velocidade = STARTING_MOVE_DISTANCE

    def criar_carros(self):
        if random.randint(1,8) == 1:
            novocarro = Turtle("square")
            novocarro.shapesize(stretch_wid=1, stretch_len=2)
            novocarro.penup()
            novocarro.color(random.choice(COLORS))
            novocarro.goto(320, random.randint(-200, 250))
            self.carros.append(novocarro)

    def car_mov(self):
        for carro in self.carros:
            carro.goto(carro.xcor() - self.velocidade, carro.ycor())

    def velocidade_mov(self):
        self.velocidade += MOVE_INCREMENT

