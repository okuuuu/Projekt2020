from tkinter import *
from yhik import yhikud
from kalkulaator import valem

class Kalk:
    def __init__(self,txt,wd,ht,rw,cm, CMD):
        self = Button(text = txt, width = wd, height = ht, command = CMD, relief=RAISED)
        self.grid(row=rw,column=cm)

root = Tk()
root.title("LTKalk")

Welcome = Label(root, text="Püütoni loodusteaduse\nkalkulaator", width = 49, height = 5, relief=GROOVE)
Welcome.grid(row=0,column=0,columnspan=2)

Kalk1 = Kalk("Ühikute\nteisendamine", 24, 3, 1, 0, yhikud)
Kalk2 = Kalk("Valemi\nkalkulaator", 24, 3, 1, 1, valem)

root.mainloop()