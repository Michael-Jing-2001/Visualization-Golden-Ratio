import turtle

def draw_fibonacci_spiral_curve(n):
    a, b = 0, 1
    golden_ratio = 1.618

    # Create a turtle screen
    screen = turtle.Screen()

    # Create a turtle object
    fibonacci_turtle = turtle.Turtle()

    # Set starting position
    fibonacci_turtle.penup()
    fibonacci_turtle.goto(0, 0)
    fibonacci_turtle.pendown()

    # Draw the Fibonacci spiral curve
    for _ in range(n):
        fibonacci_turtle.circle(a, 90)  # Draw a quarter circle with radius 'a'
        a, b = b, a + b

    # Keep the window open
    turtle.done()

# Set the number of curves in the Fibonacci spiral
curves = 15

# Draw the Fibonacci spiral curve with the specified number of curves
draw_fibonacci_spiral_curve(curves)
