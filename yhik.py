# prefix = {'T':1e12,'G':1e09,'M':1e06,'k':1e03,'':1,'m':1e-03,'μ':1e-06,'n':1e-09,'p':1e-12}
# 
# print("This app converts units to their main form.")
# INPUT = input("Please, enter your desired quantity with the units: ")
# INPUT = INPUT.split()
# print("Choose the unit in which to perform the transfer:")
# for x in prefix:
#     if len(INPUT[1])>1 and INPUT[1][0] in prefix:
#         print(x + INPUT[1][1:len(INPUT[1])])
#     else:
#         print(x + INPUT[1])
# OUTPUT = input("Unit: ")
# sigfig = len(INPUT[0])
# value = float(INPUT[0])*prefix[INPUT[1][0]]/prefix[OUTPUT[0]]
# print("Your quantity in main units is: {:.{}E} {}".format(value, sigfig-1, OUTPUT))

###########
from tkinter import *
def yhikud():
    INPUT, dec = None, None
    OUTPUT = StringVar()
    OUTPUT.set("null")
    
    def enter(event):
        nonlocal INPUT, OUTPUT, dec
        INPUT = entry1.get()
        INPUT = INPUT.split()
        if '.' in INPUT[0]:
            dec = 10**int(len(INPUT[0].split('.')[1]))
        else:
            dec = 1
        INPUT[0] = float(INPUT[0])*dec
        i = 0
        for x in prefix:
            notmain = x + INPUT[1][1:len(INPUT[1])]
            main = x + INPUT[1]
            if len(INPUT[1])>1 and INPUT[1][0] in prefix:
                Radiobutton(aken, text = notmain, variable = OUTPUT, value = notmain, command = lambda: sel(OUTPUT.get())).grid(column=1, row=i)
            else:
                Radiobutton(aken, text = main, variable = OUTPUT, value = main, command = lambda: sel(OUTPUT.get())).grid(column=1, row=i)
            i+=1
    def sel(new_units):
        if len(INPUT[1])>1 and INPUT[1][0] in prefix:
            if len(new_units)>1 and new_units[0] in prefix:
                value = INPUT[0]*prefix[INPUT[1][0]]/prefix[new_units[0]]/dec
            else:
                value = INPUT[0]*prefix[INPUT[1][0]]/dec
        else:
            if len(new_units)>1 and new_units[0] in prefix:
                value = INPUT[0]/prefix[new_units[0]]/dec
            else:
                value = INPUT[0]/dec
        sigfig = len(str(int(INPUT[0])))
        print(INPUT[0], sigfig)
        entry2.delete(0, END)
        entry2.insert(0, "{:.{}E} {}".format(value, sigfig-1, new_units))
        
    prefix = {'T':1e12,'G':1e09,'M':1e06,'k':1e03,'':1,'m':1e-03,'μ':1e-06,'n':1e-09,'p':1e-12}
    aken = Toplevel()
    aken.title("Ühikud")
    entry1 = Entry(aken, width = 30)
    entry1.bind("<Return>", enter)
    entry1.grid(row=0, column=0)
    message = Label(aken, text = "See kalkulaator teisendab ühikuid.\nPalun, sisesta üleval suurus koos ühikutega\nja vajuta ENTER.")
    message.grid(row=1, column=0, rowspan=7)
    entry2 = Entry(aken, width = 30)
    entry2.grid(row=8, column=0)
    
    aken.mainloop()