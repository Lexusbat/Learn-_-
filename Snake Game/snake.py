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
       """Moves Snake"""                      #2       
       for snake_num in range(len(snake_parts)- 1, 0, -1 ): # start= 1,stop= 3 , step= 1 BUT Check above tuple (backwards)
         new_x = snake_parts[snake_num - 1].xcor()
         new_y = snake_parts[snake_num - 1].ycor()
         snake_parts[snake_num].goto(new_x, new_y)
         snake_parts[0].forward(20)

       
