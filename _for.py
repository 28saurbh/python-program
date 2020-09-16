import turtle

square_turtle = turtle.Turtle()
square_turtle.speed(1)


def square():
    square_turtle.forward(100)
    square_turtle.right(90)
    square_turtle.forward(100)
    square_turtle.right(90)
    square_turtle.forward(100)
    square_turtle.right(90)
    square_turtle.forward(100)
    square_turtle.right(90)
    square_turtle.right(90)


for count in range(8):
    print(count)
    square()
