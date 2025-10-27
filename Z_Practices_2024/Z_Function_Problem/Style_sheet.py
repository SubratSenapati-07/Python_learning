import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy Holi!")

# Create turtle for drawing
t = turtle.Turtle()
t.speed(0)
t.width(4)
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

# Function to draw colorful circles
def draw_circle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(random.choice(colors))
    t.begin_fill()
    t.circle(random.randint(10, 50))
    t.end_fill()

# Function to create multiple color splashes
def holi_splash():
    for _ in range(100):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        draw_circle(x, y)

# Function to display "Happy Holi" text
def show_text():
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.color("white")
    t.write("Happy Holi!", font=("Arial", 30, "bold"), align="center")

# Run the Holi effect
holi_splash()
time.sleep(1)
show_text()

# Hide turtle and keep window open
t.hideturtle()
turtle.done()