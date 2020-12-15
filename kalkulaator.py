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
main()
