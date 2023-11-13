from tkinter import *
from tkinter import ttk
import random
win= Tk()
win.geometry("750x500")

opt=["rock","paper","scissor"]

def verdict(hum:str):
    human=hum.lower()
    r=random.randint(0,2)
    pc=opt[r]
    if pc==human:
        return pc+"\ndraw"
    elif (pc=="rock" and human=="paper") or (pc=="paper" and human=="scissor") or (pc=="scissor" and human=="rock"):
        return pc+"\nYou win"
    else:
        return pc+"\nPC wins" 
def lets_play():
#    while True:
    global entry
    human= entry.get()
    # if(opt[r]==human):

    txt="human: "+human+"\n"+"PC: "+verdict(human)
    label.configure(text=txt)

label=Label(win, text="", font=("Courier 22 bold"))
label.pack()
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

ttk.Button(win, text= "Play",width= 20, command= lets_play).pack(pady=20)

win.mainloop()
