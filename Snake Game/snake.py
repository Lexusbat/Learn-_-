from turtle import Turtle
class Snake: 
    start_pos =  [(0,0),(-20,0),(-40,0)] # Start pos Tuple 0,1,2

    def __init__(self,snake_part,snake_parts):
       """Creates Snake"""
       for  positions in self.start_pos:
        self.snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(positions)
        snake_parts.append(snake_part)

        pass

    def move():
