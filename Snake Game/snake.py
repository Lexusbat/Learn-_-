from turtle import Turtle
class Snake: 

    def __init__(self,start_pos,snake_parts):
       """Creates Snake"""
       for  positions in start_pos:
        self.snake_part = Turtle("square")
        self.snake_part.color("white")
        self.snake_part.penup()
        self.snake_part.goto(positions)
        self.snake_parts.append(self.snake_part)

        pass

    def move(self,snake_parts):
       """Moves Snake"""                      #2       
       for snake_num in range(len(self.snake_parts)- 1, 0, -1 ): # start= 1,stop= 3 , step= 1 BUT Check above tuple (backwards)
         new_x = self.snake_parts[snake_num - 1].xcor()
         new_y = self.snake_parts[snake_num - 1].ycor()
         self.snake_parts[snake_num].goto(new_x, new_y)
         self.snake_parts[0].forward(20)

       
