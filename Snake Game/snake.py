from turtle import Turtle

start_pos =  [(0,0),(-20,0),(-40,0)] # Start pos Tuple 0,1,2
move_dist = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake: 
    def __init__(self):
       """Attributes"""
       self.snake_parts = [] #List of all snake part (3)- will be able tc control form this list
       self.create_snake() #Function for attributes
       self.head = self.snake_parts[0]



    def create_snake(self):
       """Creates Snake"""
       for  positions in start_pos:
        self.snake_part = Turtle("square")
        self.snake_part.color("white")
        self.snake_part.penup()
        self.snake_part.goto(positions)
        self.snake_parts.append(self.snake_part)

        pass

    def move(self):
       new_x = 0
       new_y = 0
       """Moves Snake"""   
       for snake_num in range(len(self.snake_parts)- 1, 0, -1 ): # start= 1,stop= 3 , step= 1 BUT Check above tuple (backwards)
         new_x = self.snake_parts[snake_num - 1].xcor()
         new_y = self.snake_parts[snake_num - 1].ycor()
         self.snake_parts[snake_num].goto(new_x, new_y)
       self.head.forward(move_dist)

    def up(self):
     if self.head.heading() != DOWN :
      self.head.setheading(UP)
    

    def right(self):
     if  self.head.heading() != LEFT :
      self.head.setheading(RIGHT)

    def left(self):
     if self.head.heading() != RIGHT :
      self.head.setheading(LEFT)

    def down(self):
     if self.head.heading() != UP :
      self.head.setheading(DOWN)
       
