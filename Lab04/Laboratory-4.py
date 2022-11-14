# Косарпур Киана - 344494 -  Вариант 4
from tkinter import *
import tkinter as tk
from random import randrange
from tkinter import *
import random
import playsound
import threading

def loopSound():
    while True:
        playsound.playsound('jinglebells.mp3', block=True)

loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
loopThread.daemon = True # shut down music thread when the rest of the program exits
loopThread.start()

window = Tk()
window.title("Santa claus in trouble HD Code Generator")
window.geometry("1024x600")

width,height=100,100 
d=str(width)+"x"+str(height+40)
x1,y1,x2,y2=5,5,width-5,height-5
gap=25


def clicked():
    keycode = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9}
    timeout = 40
    code = ''
    for i in range(3):
        sum = 1000
        block = ''
        while sum > timeout:
            sum = 0
            block = ''
            for j in range(4):
                num = random.randint(1, 36)
                c = 0
                for k in keycode.keys():
                    c += 1
                    if c == num:
                        block += k
                        sum += keycode.get(k)
        if i != 2:
            code += block + '-'
        else:
            code += block
    canvas1.itemconfig(label1_canvas, text=code)
    animation()

def animation():
    canvas1.move(rectangle, 1, 0)
    if canvas1.coords(rectangle)[2] <  1024:
        window.after(10, animation)
 
bg = tk.PhotoImage(file='bg.png')
canvas1 = Canvas(window, width=1024, height=600)
canvas1.pack(fill="both", expand=False)
canvas1.create_image(0, 0, image=bg, anchor="nw")

color_c='#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256))                                    
rectangle = canvas1.create_rectangle(x1, y1, x2,y2,fill=color_c)
x1,y1,x2,y2=x1+gap,y1+gap,x2-gap,y2-gap
  
btn = Button(window, text="Generate", font=("Arial", 15), command=clicked)
button1_canvas = canvas1.create_window(490, 350, anchor="nw", window=btn)
label1_canvas = canvas1.create_text(540, 300, text="Click to generate the unique keycode", fill="white",font=('Arial 20 bold'))
window.mainloop()