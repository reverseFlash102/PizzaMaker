import turtle
import random
import math

# Function to draw a filled circle
def draw_circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)  # Move to the top of the circle
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to check if a new topping overlaps with existing ones
def is_overlapping(new_x, new_y, radius, existing_toppings):
    for x, y, r in existing_toppings:
        distance = math.sqrt((new_x - x) ** 2 + (new_y - y) ** 2)
        if distance < (radius + r):  # Check if circles overlap
            return True
    return False

# Function to draw random toppings without overlapping
def draw_topping(t, count, radius, color, existing_toppings):
    placed = 0
    while placed < count:
        x = random.randint(-150, 150)
        y = random.randint(-150, 150)
        if x**2 + y**2 < 150**2 and not is_overlapping(x, y, radius, existing_toppings):  # Inside pizza and no overlap
            draw_circle(t, x, y, radius, color)
            existing_toppings.append((x, y, radius))  # Add the new topping to the list
            placed += 1

# Setup turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Pizza")

# Create a turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw pizza crust
draw_circle(t, 0, 0, 200, "sandybrown")

# Draw cheese layer
draw_circle(t, 0, 0, 180, "gold")

# Track all toppings to avoid overlap
toppings = []

# Draw pepperoni
draw_topping(t, count=10, radius=20, color="firebrick", existing_toppings=toppings)

# Draw olives
draw_topping(t, count=8, radius=10, color="darkgreen", existing_toppings=toppings)

# Finalize with mainloop to keep the window open
screen.mainloop()
