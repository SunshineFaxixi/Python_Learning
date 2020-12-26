import turtle as t
import random

colors = ["cornflowerBlue", "dark gray", "blue", "magenta", "dark orchid", "salmon"]
directions = [0, 90, 180, 270]

tim = t.Turtle()
t.colormode(255)
# tim.shape("turtle")
# tim.color("red")
# tim.forward(100)
# tim.right(90)

# # draw a sqare
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# # draw dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


def draw_shape(num_sizes):
    angle = 360 / num_sizes
    for _ in range(num_sizes):
        tim.forward(100)
        tim.right(angle)


def draw_random_walk(num_step):
    tim.pensize(15)
    tim.speed("fastest")
    for _ in range(num_step):
        tim.color(random_color())
        tim.setheading(random.choice(directions))
        tim.forward(50)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(size_of_gap):
    tim.speed("fastest")
    tim.pensize(3)
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

# for shape_side_n in range(3, 11):
#     color = tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


# draw_random_walk(100)
draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()