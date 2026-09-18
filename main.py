import turtle
t = turtle.Turtle()
t.speed(100)
def kletka():
   for i in range(4):
     t.forward(20)
     t.left(90)
for i in range(8):
   kletka()
   t.forward(20)

y_step = 0
for i in range(7):
   t.penup()
   y_step = y_step +20
   t.goto(0,y_step)
   t.pendown()

   for i in range(8):
      kletka()
      t.forward(20)
t.penup()
t.goto(-15,-15)
t.pendown()
t.goto(0,0)
t.goto(-15,-15)
t.goto(-15,175)
t.goto(175,175)
t.goto(175,-15)
t.goto(-15,-15)
t.goto(-15,175)
t.goto(0,160)
t.goto(-15,175)
t.goto(175,175)
t.goto(160,160)
t.goto(175,175)
t.goto(175,-15)
t.goto(165,-5)
turtle.mainloop()


