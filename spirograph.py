import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(10):
     for colors in ['red', 'yellow', 'blue', 'purple', 'green', 'orange']:
         turtle.color(colors)
         turtle.circle(100)
         turtle.left(10)

turtle.hideturtle()
