import turtle
import random


screen = turtle.Screen()
screen.setup(width=500, height=400)
color_list = ["blue", "green", "yellow", "red", "pink", "purple"]
is_pace_on =False
user_bet = screen.textinput(title="Make a bet", prompt="Which color do you think may win?")
turtle_list = []

for index in range(len(color_list)):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(color_list[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-75 + index * 30)
    turtle_list.append(new_turtle)

if user_bet:
    is_pace_on = True

while is_pace_on:
    for t in turtle_list:
        if t.xcor() > 230:
            is_pace_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won, {winning_color} is the winning color")
            else:
                print(f"You've lost, {winning_color} is the winning color")
        pace = random.randint(1, 10)
        t.forward(pace)


screen.exitonclick()