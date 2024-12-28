import turtle
from typing import List, Tuple


class SnakeHead:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("square")
        self.turtle.color("green")
        self.turtle.penup()
        self.turtle.goto(0, 0)
        self.direction = "stop"

    def move(self, distance: int = 20):
        if self.direction == "up":
            self.turtle.sety(self.turtle.ycor() + distance)
        elif self.direction == "down":
            self.turtle.sety(self.turtle.ycor() - distance)
        elif self.direction == "left":
            self.turtle.setx(self.turtle.xcor() - distance)
        elif self.direction == "right":
            self.turtle.setx(self.turtle.xcor() + distance)

    def set_direction(self, new_direction: str):
        opposite_directions = {"up": "down", "down": "up", "left": "right", "right": "left"}
        if self.direction != opposite_directions.get(new_direction):
            self.direction = new_direction


class Food:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("circle")
        self.turtle.color("red")
        self.turtle.penup()
        self.turtle.goto(0, 100)

    def random_position(self, bounds: Tuple[int, int]):
        import random
        x = random.randint(-bounds[0], bounds[0])
        y = random.randint(-bounds[1], bounds[1])
        self.turtle.goto(x, y)


class Scoreboard:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("square")
        self.turtle.color("green")
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(0, 260)
        self.score = 0
        self.high_score = 0

        # Game over message turtle
        self.game_over_turtle = turtle.Turtle()
        self.game_over_turtle.speed(0)
        self.game_over_turtle.color("red")
        self.game_over_turtle.penup()
        self.game_over_turtle.hideturtle()
        self.game_over_turtle.goto(0, 0)

    def update(self):
        self.turtle.clear()
        self.turtle.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            align="center",
            font=("ds-digital", 24, "normal")
        )

    def show_game_over(self):
        self.game_over_turtle.clear()
        self.game_over_turtle.write(
            "GAME OVER",
            align="center",
            font=("Arial", 40, "bold")
        )

    def hide_game_over(self):
        self.game_over_turtle.clear()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()
        self.hide_game_over()


class SnakeBody:
    def __init__(self):
        self.segments: List[turtle.Turtle] = []

    def add_segment(self):
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("green")
        segment.penup()
        self.segments.append(segment)

    def move_segments(self, head: SnakeHead):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        if self.segments:
            self.segments[0].goto(head.turtle.xcor(), head.turtle.ycor())

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()