import turtle

t = turtle.Turtle()
t.speed(3)

# ১. সবুজ অংশ (নিচের অংশ)
t.penup()
t.goto(-200, -120) 
t.fillcolor("green")
t.begin_fill()
t.pendown()
for _ in range(2):
    t.forward(400)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

# ২. সাদা অংশ (মাঝের অংশ)
t.penup()
t.goto(-200, -40) 
t.fillcolor("white")
t.begin_fill()
t.pendown()
for _ in range(2):
    t.forward(400)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

# ৩. কমলা অংশ (উপরের অংশ)
t.penup()
t.goto(-200, 40)
t.fillcolor("orange")
t.begin_fill()
t.pendown()
for _ in range(2):
    t.forward(400)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

# ৪. আকাশী নীল বৃত্ত (মাঝখানে)
t.penup()
t.goto(40, 0) 
t.setheading(90) 
t.pencolor("skyblue")
t.pensize(3)
t.fillcolor("skyblue")
t.begin_fill() # এখানে ব্র্যাকেট () যোগ করা হয়েছে
t.pendown()
t.circle(40)
t.end_fill()

t.hideturtle()
turtle.mainloop()