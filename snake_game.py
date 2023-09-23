from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")


def play():
    scoreboard.show_score()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # collision with food
        if snake.head.distance(food) < 20:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()

        # collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
            snake.reset()
            scoreboard.reset()

        # collision with itself
        for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                snake.reset()
                scoreboard.reset()

def close_window():
    screen.bye()


scoreboard.start_game()
screen.onkey(play, "space")
screen.onkey(close_window, 'Escape')

# run
screen.mainloop()
