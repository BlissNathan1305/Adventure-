import turtle

def draw_polygon(sides, size):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(size)
        turtle.left(angle)

# Draw a hexagon (6 sides)
turtle.speed(2)  # Set the drawing speed
draw_polygon(6, 100)  # Draw a hexagon with side length 100

turtle.done()
