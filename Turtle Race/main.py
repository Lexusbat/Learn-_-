from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win? Bet on it! Choose a colour: ")
colors = ["black","red","blue","purple","yellow","green"] # 6 color turtles
y_pos = [-70,-40,-10,20,50,80]
all_turtles =[]



def Turtle_pos(index):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[index])
    new_turtle.goto(-200,y_pos[index])
    all_turtles.append(new_turtle)

    
is_race_on = False

"""
def race():
    spaces_new_turtle  = random.randint(5, 20)   # Returns an integer from 0 to 10 (inclusive)
    new_turtle.speed(1)
    new_turtle.forward(spaces_new_turtle)
    spaces_tim = random.randint(5, 20)   # Returns an integer from 0 to 10 (inclusive)

new_turtle = Turtle()
tim = Turtle()
new_turtle.penup()
new_turtle.goto(x=-200,y=0)
tim.penup()
tim.goto(x=-200,y=-50)
"""
if user_bet:
     is_race_on = True

for index in range(6):
      Turtle_pos(index)

win_color = ""
while is_race_on ==  True: 
    spaces_new_turtle  = random.randint(0, 10)   # Returns an integer from 0 to 10 (inclusive)
    for turtle in all_turtles:
        if turtle.xcor() > 200:
             win_color = turtle.pencolor()
             if user_bet != win_color:
                  print(f"Awwww you lose! {win_color} turtle won")
                  is_race_on = False
             else:
                  print(f"Yay, you win.Your {win_color} turtle won")
                  is_race_on = False
      
    

        spaces_new_turtle  = random.randint(0, 10)   # Returns an integer from 0 to 10 (inclusive)
        turtle.forward(spaces_new_turtle)






screen.exitonclick()