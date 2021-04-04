import tkinter
import random
colours=['Red','Yellow','Orange','Blue','Pink','Green','Black','Purple','White']
score=0
timeleft=60
def startgame(event):
    if timeleft == 60:
        countdown()
    nextcolour()
def nextcolour():
    global score
    global timeleft
    if timeleft>0:
        c.focus_set()
        if c.get().lower()==colours[1].lower():
            score+=1
        c.delete(0,tkinter.END)
        random.shuffle(colours)
        Label.config(fg=str(colours[1]),text=str(colours[0]))
        scoreLabel.config(text="score:"+str(score))
def countdown():
    global timeleft
    if timeleft>0:
        timeleft-=1
        timeLabel.config(text="Time left:"+str(timeleft))
        timeLabel.after(1000,countdown)
t=tkinter.Tk()
t.title("Colour Game")
t.geometry("400x200")
instructions=tkinter.Label(t,text="Type the colour of words, not the word colour",font=("ariel",12))
instructions.pack()
scoreLabel=tkinter.Label(t,text="Press Enter to start",font=("ariel",12))
scoreLabel.pack()
timeLabel=tkinter.Label(t,text="Time left:"+ str(timeleft),font=("ariel",12))
timeLabel.pack()
Label=tkinter.Label(t,font=("ariel",60))
Label.pack()
c=tkinter.Entry(t)
t.bind('<Return>',startgame)
c.pack()
c.focus_set()
t.mainloop()
