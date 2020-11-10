from tkinter import *
from yhik import yhikud
from kalkulaator import valem


def fcn3():
    return

class Kalk:
    def __init__(self,txt,wd,ht,rw,cm, CMD):
        self = Button(text = txt, width = wd, height = ht, command = CMD)
        self.grid(row=rw,column=cm)

root = Tk()
root.title("LTKalk")

Welcome = Label(root, text="Püütoni loodusteaduse\nkalkulaator", width = 48, height = 5, relief=GROOVE)
Welcome.grid(row=0,column=0,columnspan=3)

Kalk1 = Kalk("Kalk1", 16, 3, 1, 0, yhikud)
Kalk2 = Kalk("Kalk2", 16, 3, 1, 1, valem)
Kalk3 = Kalk("Kalk3", 16, 3, 1, 2, fcn3)

root.mainloop()