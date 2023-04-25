from tkinter import *
from datetime import datetime
import pyglet
pyglet.font.add_file("digital-7.ttf")


def clock():
    time = datetime.now()
    hour = time.strftime('%H:%M:%S')
    day_week = time.strftime('%A')
    day = time.day
    month = time.strftime('%b')
    year = time.strftime('%Y')

    l1.config(text=hour)
    l1.after(200, clock)
    l2.config(text=day_week + "  " + str(day) + "/" + str(month) + "/" + str(year))


Color1 = "#3d3d3d"  # black
Color2 = "#fafcff"  # white
Color3 = "#21c25c"  # green
Color4 = "#eb463b"  # red
Color5 = "#dedcdc"  # gray
Color6 = "#3080f0"  # blue


background = Color1
color = Color2

window = Tk()
window.title('')
window.geometry('550x200')
window.resizable(width=False, height=False)
window.configure(bg=Color1)

l1 = Label(window, text="", font="digital-7 100", bg=background, fg=color)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(window, text="", font="Arial 17", bg=background, fg=color)
l2.grid(row=1, column=0, sticky=NW, padx=5)

clock()
window.mainloop()
