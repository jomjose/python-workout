import turtle

def draw_square():
    #new object init
    brad = turtle.Turtle()

    #brad properties
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)

    #draw square
    for x in range(0, 4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    #new object init
    angie = turtle.Turtle()

    #angie properties
    angie.shape("arrow")
    angie.color("green")

    #draw circle
    angie.circle(100)

def draw_triangle():

    #new object init
    orangie = turtle.Turtle()

    #orangie properties
    orangie.shape("turtle")
    orangie.color("red")

    #draw triangle
    for x in range(0,3):
        orangie.forward(100)
        orangie.right(120)
