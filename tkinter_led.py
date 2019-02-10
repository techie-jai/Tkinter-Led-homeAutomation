#for python version 3, change Tkinter to tkinter(only change in import, not below)
from Tkinter import * #change here
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

window = Tk() #not here
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=10)
 
txt.grid(column=1, row=0)
 
def clicked():
 
    res = "Welcome to " + txt.get()
 
    lbl.configure(text= res)

def blink():
    print "LED on"
    GPIO.output(17,GPIO.HIGH)
    time.sleep(2)
    print "LED off"
    GPIO.output(17,GPIO.LOW)
    time.sleep(2)
    
 
btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=2, row=0)

btn2 = Button(window, text="LED", command=blink)

btn2.grid(column=3, row=0)
 
window.mainloop()
