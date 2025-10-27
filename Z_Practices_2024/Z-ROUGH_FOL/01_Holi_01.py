import turtle
import random
import time
from turtle import Screen

def draw_color_burst(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    for _ in range(12):  # More bursts
        turtle.forward(40)
        turtle.backward(40)
        turtle.left(30)

def draw_splashes():
    colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#FFA500", "#800080"]
    for _ in range(25):  # More random splashes
        x = random.randint(-350, 350)
        y = random.randint(-250, 250)
        color = random.choice(colors)
        draw_color_burst(x, y, color)

def write_text(name):
    turtle.penup()
    turtle.goto(-220, 0)
    turtle.pendown()
    turtle.color("gold")
    turtle.write(f"🎨✨ Happy Holi, {name}! ✨🎨", font=("Comic Sans MS", 35, "bold"))

def animated_background():
    colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#A833FF", "#FFD700", "#FF4500", "#00CED1"]
    for _ in range(20):  # Faster background changes
        screen.bgcolor(random.choice(colors))
        time.sleep(0.15)

def firework_effect():
    for _ in range(8):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(random.choice(["red", "yellow", "cyan", "magenta", "white"]))
        turtle.dot(random.randint(20, 50))
        time.sleep(0.1)

def main():
    global screen
    screen = Screen()
    screen.setup(width=900, height=600)
    screen.bgcolor("black")  # Dark background for more vibrancy
    turtle.speed(0)
    turtle.delay(0)
    
    name = input("Enter your name: ")  # Get user's name
    animated_background()
    draw_splashes()
    firework_effect()
    write_text(name)
    turtle.done()

if __name__ == "__main__":
    main()
