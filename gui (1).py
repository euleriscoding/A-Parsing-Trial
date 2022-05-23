import tkinter as tk
from tkinter import BOTH, BOTTOM, HORIZONTAL, LEFT, RIGHT, TOP, VERTICAL, PanedWindow, ttk
from tkinter import filedialog as fd
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
import turtle
import lex
#import yacc, lexing, parsing



############   GUI TASARIMI ##############
def choose_file():
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=(("text files",".txt"),
        ("all files",".*")))

    file = open(filename,'r')
    print(file.read())
    global data
    data = file.read()

    file.close()



root = tk.Tk()
root.title("Automata Theory")
root.geometry("600x500")

##################### TURTLE'I GUI'YE EKLEME ##################
canvas = ScrolledCanvas(root) 
canvas.pack(side=LEFT, fill=BOTH) 
screen = TurtleScreen(canvas) 
turtle = RawTurtle(canvas) 

turtle.up()

open_button = ttk.Button(
    root,
    text='Dosya Seç',
    command=choose_file
)


panel_2 = PanedWindow(bd=4, relief="raised")
panel_2.pack(fill=BOTH, expand= 1)
#KONTROL PANELI
right_panel = PanedWindow(panel_2, orient=HORIZONTAL, bd=2, relief="raised", bg="light blue")
panel_2.add(right_panel)



#HATA PANELI
bottom_panel = PanedWindow(panel_2, orient=VERTICAL, bd=2, relief="raised", height= "100", bg= "light green")
panel_2.add(bottom_panel)
bottom_panel.pack(fill= BOTH, side= BOTTOM)

open_button.pack(pady= "10")


root.mainloop()