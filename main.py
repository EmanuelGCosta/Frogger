import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

placar = Scoreboard()
jogador = Player()
carro = CarManager()

screen.listen()
screen.onkey(jogador.movimento, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.016)
    screen.update()

    carro.criar_carros()
    carro.car_mov()

    for car in carro.carros:
        if car.distance(jogador) < 20:
            placar.game_over()
            game_is_on = False

        if car.xcor() < -320:
            car.hideturtle()

    if jogador.ycor() > 280:
        jogador.initial_pos()
        placar.level_up()
        carro.velocidade_mov()

screen.exitonclick()
