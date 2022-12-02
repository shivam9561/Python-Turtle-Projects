import turtle
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

t = turtle.Pen()
t.speed(10)

turtle.bgcolor("black")

# make spiral_web
for x in range(200):
    t.pencolor(colors[x % 6])  # setting color
    t.width(x / 100 + 2)  # setting width
    t.forward(x)  # moving forward
    t.left(59)  # moving left

turtle.done()
t.speed(10)

turtle.bgcolor("black") 

# make spiral_web
for x in range(200):
    t.pencolor(colors[x % 6])  # setting color
    t.width(x / 100 + 1)  # setting width
    t.forward(x)  # moving forward
    t.left(59)  # moving left

turtle.done()
