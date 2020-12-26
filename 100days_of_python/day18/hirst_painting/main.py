import turtle
import random

turtle.colormode(255)
color_list = [(131, 165, 205), (224, 150, 101), (32, 41, 59), (199, 134, 147), (234, 212, 88), (167, 56, 46), (39, 104, 153), (141, 184, 162), (150, 59, 66), (169, 29, 33), (215, 81, 71), (157, 32, 30), (236, 165, 157), (15, 96, 70), (58, 50, 47), (50, 111, 90), (49, 42, 47), (34, 61, 56), (227, 165, 169), (170, 188, 221), (184, 103, 112), (32, 59, 108), (105, 127, 160), (175, 200, 188), (33, 150, 210), (65, 66, 56)]


tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
num_of_dot = 100


for dot_count in range(1, num_of_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()