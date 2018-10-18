import turtle

# get a handle on the window that opens, so you can control it
window = turtle.Screen()


def square(turtl, size):
    for i in range(4):
        turtl.forward(size)
        turtl.right(90)


def circle_out_of_squares(turtl, speed, square_size, step_angle):
    turtl.speed(speed)
    step_angle = step_angle
    for i in range(360//step_angle):
        square(turtl, square_size)
        turtl.right(step_angle)


def square_out_of_circles(turtl, speed, square_size):
    pass  # TODO


# prevent the window from closing until you mouse-click on it
window.exitonclick()