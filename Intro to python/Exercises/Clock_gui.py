from tkinter import *
from time import strftime

def update():
    timeString = strftime("%I:%M:%S %p")
    timeLabel.config(text=timeString)

    dayString = strftime("%A")
    dayLabel.config(text=dayString)

    dateString = strftime("%B %d, %Y")
    datelabel.config(text=dateString)

    window.after(1000, update)

window = Tk()

timeLabel = Label(window, font=("Arial", 50), fg="#00ff00", bg="black")
timeLabel.pack()

dayLabel = Label(window, font=("LCD", 25 ))
dayLabel.pack()

datelabel = Label(window, font=("LCD", 30))
datelabel.pack()

update()
window.mainloop()