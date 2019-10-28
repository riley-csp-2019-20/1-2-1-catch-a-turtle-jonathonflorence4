# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
turtleshape= 'square'
turtlesize= 5
turtlecolor= "blue"

score = 0

font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
neo= trtl.Turtle(shape=turtleshape)
neo.color(turtlecolor)
neo.shapesize(turtlesize)
neo.speed(0)

score_writer = trtl.Turtle()
score_writer.ht()
score_writer.penup()
score_writer.goto(-370, 270)

font_setup= ("Arial", 30, "bold")
score_writer.write(score, font=font_setup)

counter =  trtl.Turtle()
counter. ht()
counter.penup()
counter.goto(250,265)
#-----game functions--------
def turtle_clicked(x,y):
    print("neo got clicked")
    change_position()
    update_score()

def change_position():
    neo.penup()
    neo.ht()
    if not timer_up: 
        neox = random.randint(-400, 400)
        neoy = random.randint(-300, 300)
        neo.goto(neox, neoy)
        neo.st()

def update_score():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer. write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 



#-----events----------------
wn = trtl.Screen()

neo.onclick(turtle_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()