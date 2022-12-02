import turtle

sc = turtle.Screen()
pen = turtle.Turtle()
def semi_circle(col, rad, val):
    # Set the fill color of the semicircle
    pen.color(col)

    # Draw a circle
    pen.circle(rad, -180)

    # Move the turtle to air
    pen.up()

    # Move the turtle to a given position
    pen.setpos(val, 0)

    # Move the turtle to the ground
    pen.down()

    pen.right(180)


# Set the colors for drawing
col = ['violet', 'indigo', 'blue',
       'green', 'yellow', 'orange', 'red']

# Setup the screen features
sc.setup(600, 600)

# Set the screen color to black
sc.bgcolor('black')

# Setup the turtle features
pen.right(90)
pen.width(10)
pen.speed(7)

# Loop to draw 7 semicircles
for i in range(7):
    semi_circle(col[i], 10 * (
            i + 8), -10 * (i + 1))
pen.hideturtle()
