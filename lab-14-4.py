# MEE 03/23/22


import turtle

window = turtle.Screen()
window.setup()
window.title("Lab 4")
frank = turtle.Turtle()
frank.speed(3)
frank.color("red")
frank.fillcolor("maroon")

frank.stamp()
frank.penup()
frank.begin_fill()
frank.setposition(100,100)
frank.pendown()
frank.forward(100)
frank.right(90)
frank.forward(100)
frank.right(90)
frank.forward(100)
frank.right(90)
frank.forward(100)
frank.end_fill()

window.mainloop()
