import turtle

def draw_heart():
    # Set up the turtle
    turtle.color("red")
    turtle.begin_fill()

    # Draw the heart shape
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)

    turtle.end_fill()
    turtle.hideturtle()

# Create the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Red Heart Symbol")

# Draw the heart
draw_heart()

# Keep the window open until it is closed by the user
turtle.done()
