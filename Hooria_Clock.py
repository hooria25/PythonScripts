from tkinter import *
from time import strftime

myWindow = Tk()
myWindow.title("Hooria's Clock")

def time():
	myTime = strftime("%H:%M:%S %p")
	clock.config(text = myTime)
	clock.after(1000, time)

clock = Label(myWindow, font = ('Times New Roman', 40, 'bold'), background = 'dark blue', foreground = 'white')

clock.pack(anchor = 'center')
time()

mainloop()