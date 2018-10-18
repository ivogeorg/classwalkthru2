import turtle

# get a handle on the window that opens, so you can control it
window = turtle.Screen()


def square(turtl, size):
    for i in range(4):
        turtl.forward(size)
        turtl.right(90)


t = turtle.Turtle()
t.speed(80)
step_angle = 3
for i in range(360//step_angle):
    square(t, 100)
    t.right(step_angle)


# prevent the window from closing until you mouse-click on it
window.exitonclick()