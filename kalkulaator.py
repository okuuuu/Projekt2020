from tkinter import *
import pickle

class Valem:
    def __init__(self, nimi, muutujad, valemid):
        self.nimi = nimi
        self.muutujad = muutujad
        self.valemid = valemid

# Kui siia lisada valemid kujul Valem("valemi nimi", "array muutujatega", "vastavate muutujate kaudu avaldused") siis oskab programm need valemid avaldada
kõik_valemid = [
    Valem("kiiruse arvutamise valem", ["s", "v", "t"], ["v*t", "s/t", "s/v"]),
    Valem("võnkeperioodi arvutamis valem", ["T", "t", "N"], ["t/N", "T*N", "t/T"])]

# usr_valem on index arrayst kõik_valemid. arvuta on kas True või False vastavalt sellele kas arvutatakse valemi väärtus või lihtsalt kuvatakse valem.
def opereeri(usr_valem, usr_var, arvuta):
    variables = {}
    valem = usr_valem.valemid[usr_var]
    if arvuta:
        for i, v in enumerate(usr_valem.muutujad):
            if i != usr_var:
                variables[v] = input(v + "- ")
        for v in variables:
            valem = valem.replace(v, variables[v])
        valem = str(eval(valem))
    print(usr_valem.muutujad[usr_var] + "= " + valem)


def lisa_valem():
    muutujad = []
    muutujate_avaldused = []
    nimi = input("Mis on valemi nimi? ")
    x = int(input("Mitu erinevat muutujat on valemis? "))
    for i in range(x):
        muutujad.append(input("Sisesta " + str(i+1) + ". muutuja tähistus: "))
    print("Kasutades Pythoni syntaxi, kuidas vastavad muutujad avalduvad: (" + ",".join(muutujad) + ")")
    for i in range(x):
        muutujate_avaldused.append(input(muutujad[i] + "= "))
    kõik_valemid.append(Valem(nimi, muutujad, muutujate_avaldused))
    with open("valemid.pickle", "wb") as f:
        pickle.dump(kõik_valemid, f)

def eemalda_valem():
    print("Kõik valemid on järgmised")
    for i, x in enumerate(kõik_valemid):
        print(str(i+1) + ". " + x.nimi)
    del kõik_valemid[int(input("Millist soovite eemaldada, sisestage jrk nr - "))-1]
    with open("valemid.pickle", "wb") as f:
        pickle.dump(kõik_valemid, f)

def main():
    global kõik_valemid
    try:
        with open("valemid.pickle", "rb") as f:
            kõik_valemid = pickle.load(f)
    except:
        with open("valemid.pickle", "wb") as f:
            pickle.dump(kõik_valemid, f)
    print("Tere!")
    print("See kalkulaator suudab viib valemi õigele kujule kui sisestate vastavad muutujad")
    print("Hetkel toetame vastavaid valemarvutusi:\n")
    for i, x in enumerate(kõik_valemid):
        print(str(i+1) + ". " + x.nimi + " " + x.muutujad[0] + "=" + x.valemid[0])
    print("\n")
    if input("-- Kas soovite valemeid lisada (y/n) - ") == "y":
        lisa_valem()
        print("\n\n\n")
        return main()
    elif input("-- Kas soovite valemeid eemaldada (y/n) - ") == "y":
        eemalda_valem()
        print("\n\n\n")
        return main()
    usr_valem = kõik_valemid[int(input("-- Millise valemiga soovite opereerida? (jrk nr) - "))-1]
    usr_var = usr_valem.muutujad.index(input("-- Millise muutuja kaudu soovite valemi avaldada (" + ",".join(usr_valem.muutujad) + ") - "))

    arvutan = True if input("-- Arvutan tulemusi koos kindlate muutujate väärtustega? (y/n) - ") == "y" else False

    opereeri(usr_valem, usr_var, arvutan)
#main()

def valem():
    class Valem:
        def __init__(self, nimi, muutujad, valemid):
            self.nimi = nimi
            self.muutujad = muutujad
            self.valemid = valemid
            
    kõik_valemid = [
    Valem("kiiruse arvutamise valem", ["s", "v", "t"], ["v*t", "s/t", "s/v"]),
    Valem("võnkeperioodi arvutamise valem", ["T", "t", "N"], ["t/N", "T*N", "t/T"])]
    
#     try:
#         with open("valemid.pickle", "rb") as f:
#             kõik_valemid = pickle.load(f)
#     except:
#         with open("valemid.pickle", "wb") as f:
#             pickle.dump(kõik_valemid, f)
    
    def lisa_valem():
        def enter1(event):
            def enter2(event):
                def enter3(event):
                    avaldused = []
                    for i in range(int(muut_arv.get())):
                        avaldused.append(avaldused_ent['a'+str(i)].get())
                    kõik_valemid.append(Valem(nimi.get(), muutujad, avaldused))
                    WelcMsg = "Tere!\nSee kalkulaator viib valemi õigele\nkujule kui sisestate vastavad muutujad\nHetkel toetame vastavaid valemarvutusi:\n"
                    for i, x in enumerate(kõik_valemid):
                        WelcMsg+=("\n" + str(i+1) + ". " + x.nimi + " " + x.muutujad[0] + "=" + x.valemid[0])
                    Welcome.config(text = WelcMsg)
                    for k in Radios:
                        Radios[k].destroy()
                    for i in range(len(kõik_valemid)):
                        Radios['r'+str(i)] = Radiobutton(aken, text = str(i+1), variable = usr_valem, value = i, command = lambda: muut(usr_valem.get()))
                        Radios['r'+str(i)].grid(column=2+i, row=1)
                    LV.destroy()
                muutujad = []
                avaldused_ent = dict()
                for i in range(int(muut_arv.get())):
                    muutujad.append(muutujad_ent['e'+str(i)].get())
                Label(LV, text = "Kasutades Pythoni syntaxi, kuidas vastavad muutujad avalduvad: (" + ",".join(muutujad) + ")").grid(column=0, row=4+int(muut_arv.get()))
                for i in range(int(muut_arv.get())):
                    Label(LV, text = muutujad[i] + "= ").grid(column=0, row=5+int(muut_arv.get())+i)
                    avaldused_ent['a'+str(i)] = Entry(LV, width = 5)
                    avaldused_ent['a'+str(i)].grid(column=1, row=5+int(muut_arv.get())+i)
                avaldused_ent['a'+str(int(muut_arv.get())-1)].bind('<Return>', enter3)
            
            muutujad_ent = dict()
            for i in range(int(muut_arv.get())):
                Label(LV, text = "Sisesta " + str(i+1) + ". muutuja tähistus: ").grid(column=0, row=3+i)
                muutujad_ent['e'+str(i)] = Entry(LV, width = 5)
                muutujad_ent['e'+str(i)].grid(column=1, row=3+i)
            muutujad_ent['e'+str(int(muut_arv.get())-1)].bind('<Return>', enter2)
        
        LV = Toplevel()
        LV.title("Lisa valem")
        Label(LV, text = "Mis on valemi nimi?").grid(column=0, row=0)
        nimi = Entry(LV, width = 20)
        nimi.grid(column=0, row=1)
        Label(LV, text = "Mitu erinevat muutujat on valemis?").grid(column=0, row=2)
        muut_arv = Entry(LV, width = 5)
        muut_arv.bind('<Return>', enter1)
        muut_arv.grid(column=1, row=2)
        
#         with open("valemid.pickle", "wb") as f:
#             pickle.dump(kõik_valemid, f)
        
    def eemalda_valem():
        def enter4(event):
            del kõik_valemid[int(e.get())-1]
            WelcMsg = "Tere!\nSee kalkulaator viib valemi õigele\nkujule kui sisestate vastavad muutujad\nHetkel toetame vastavaid valemarvutusi:\n"
            for i, x in enumerate(kõik_valemid):
                WelcMsg+=("\n" + str(i+1) + ". " + x.nimi + " " + x.muutujad[0] + "=" + x.valemid[0])
            Welcome.config(text = WelcMsg)
            for k in Radios:
                Radios[k].destroy()
            for i in range(len(kõik_valemid)):
                Radios['r'+str(i)] = Radiobutton(aken, text = str(i+1), variable = usr_valem, value = i, command = lambda: muut(usr_valem.get()))
                Radios['r'+str(i)].grid(column=2+i, row=1)
            EV.destroy()
            
        EV = Toplevel()
        EV.title("Eemalda valem")
        Label(EV, text = "Millist valemit soovite eemaldada? Sisestage jrk nr.").pack()
        e = Entry(EV, width = 5)
        e.pack()
        e.bind('<Return>', enter4)
#         with open("valemid.pickle", "wb") as f:
#             pickle.dump(kõik_valemid, f)
    
    def muut(valem):
        for i, x in enumerate(kõik_valemid[valem].muutujad):
            Radiobutton(aken, text = x, variable = usr_var, value = kõik_valemid[valem].muutujad.index(x), command = lambda: opereeri(kõik_valemid[valem], usr_var.get(), operation.get())).grid(column=2+i, row=3)
        Radiobutton(aken, text = "Kuvan lihtsalt valemi", variable = operation, value = 0, command = lambda: opereeri(kõik_valemid[valem], usr_var.get(), operation.get())).grid(column=2, row=4)
        Radiobutton(aken, text = "Arvutan kindlate väärtustega", variable = operation, value = 1, command = lambda: opereeri(kõik_valemid[valem], usr_var.get(), operation.get())).grid(column=3, row=4)
    
    def opereeri(usr_valem, usr_var, oper):
        def arvuta():
            valem = usr_valem.valemid[usr_var]
            for i, v in enumerate(usr_valem.muutujad):
                if i != usr_var:
                    variables[v] = Entries["e"+str(i)].get()
            for v in variables:
                valem = valem.replace(v, variables[v])
            valem = str(eval(valem))
            Answer.config(text = (usr_valem.muutujad[usr_var] + "= " + valem))
        variables = {}
        valem = usr_valem.valemid[usr_var]
        for k in Entries:
                Entries[k].destroy()
        if oper == 1:
            for i, v in enumerate(usr_valem.muutujad):
                if i != usr_var:
                    Entries["e"+str(i)] = Entry(aken, width = 30)
                    Entries["e"+str(i)].insert(0, "SISESTA " + v + " VÄÄRTUS SIIA")
                    Entries["e"+str(i)].grid(column=2, row=5+i)
            Entries["Arvuta"] = Button(aken, text = "Arvuta", command = arvuta)
            Entries["Arvuta"].grid(column=2, row=99)
        Answer = Label(aken, text=(usr_valem.muutujad[usr_var] + "= " + valem), width = 50)
        Answer.grid(column=0, row=100, columnspan=100)
    
    aken = Toplevel()
    aken.title("Valemid")
    WelcMsg = "Tere!\nSee kalkulaator viib valemi õigele\nkujule kui sisestate vastavad muutujad\nHetkel toetame vastavaid valemarvutusi:\n"
    for i, x in enumerate(kõik_valemid):
        WelcMsg+=("\n" + str(i+1) + ". " + x.nimi + " " + x.muutujad[0] + "=" + x.valemid[0])
    Welcome = Label(aken, text = WelcMsg)
    Welcome.grid(row=0, column=0, rowspan=50, columnspan = 2)
    ValLis = Button(aken, text = "Lisada valemeid", command = lisa_valem).grid(column=0, row=99)
    ValEem = Button(aken, text = "Eemaldada valemeid", command = eemalda_valem).grid(column=1, row=99)
    Label(aken, text = "Valige vastav valem:").grid(row=0, column=2, columnspan=50)
    usr_valem = IntVar()
    usr_valem.set(0)
    usr_var = IntVar()
    usr_var.set(0)
    operation = IntVar()
    operation.set(0)
    Entries = dict()
    Radios = dict()
    for i in range(len(kõik_valemid)):
        Radios['r'+str(i)] = Radiobutton(aken, text = str(i+1), variable = usr_valem, value = i, command = lambda: muut(usr_valem.get()))
        Radios['r'+str(i)].grid(column=2+i, row=1)
    Label(aken, text = "Millise muutuja kaudu soovite valemi avaldada?").grid(row=2, column=2, columnspan=3)
    
    mainloop()
