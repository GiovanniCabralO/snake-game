from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import pygame

pygame.mixer.init()

pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

eat_sound = pygame.mixer.Sound("blip.wav")
game_over_sound = pygame.mixer.Sound("gameover.wav")


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
difficulty = screen.textinput("Difficulty", "Choice: easy / medium / hard.").lower()
if difficulty == "easy":
    speed = 0.2
elif difficulty == "medium":
    speed = 0.1
else:
    speed = 0.05

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        eat_sound.play()


    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        pygame.mixer.music.stop()
        game_over_sound.play()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            pygame.mixer.music.stop()
            game_over_sound.play()
            


screen.exitonclick()
