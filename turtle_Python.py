import turtle

# “Turtle” is a python feature like a drawing board, which lets you command a turtle to draw all over it!

a = turtle.Turtle()  # making turtle object
a.speed(1)  # defining the speed at which the diagrams are drawn


def square():  # creating square function
    a.forward(100)  # draw a line of 100 length
    a.right(90)  # turn right in 90 degree
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.right(90)


square()  # calling the function

# we want to make the square and walk forward and make another square
a.forward(200)
square()
