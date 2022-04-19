import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(0)

color = ("#3cd070", "#ccff00", "#ee4b2b", "#ff3503", "#7df9ff", "#0ff0fc",
         "#cf6ba9", "#ea00ff", "#6a0dad", "#fff01f", "#b1bc55", "#76b583")

for i in range(120):
    t.pencolor(color[i&6])
    t.circle(190-1/2, 90)
    t.left(90)
    t.circle(190-i/3, 90)
    t.left(60)

s.exitonclick()
