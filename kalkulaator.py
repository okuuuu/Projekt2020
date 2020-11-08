class Valem:
    def __init__(self, nimi, muutujad, valemid):
        self.nimi = nimi
        self.muutujad = muutujad
        self.valemid = valemid

# Kui siia lisada valemid kujul Valem("valemi nimi", "array muutujatega", "vastavate muutujate kaudu avaldused") siis oskab programm need valemid avaldada
kõik_valemid = [
    Valem("kiiruse valem", ["s", "v", "t"], ["v*t", "s/t", "s/v"])]

def arvuta(usr_choice):
    variables = []
    print("Sisestage järgnevate muutujate väärtused, kui väärtust ei eksisteeri siis ärge sisestage midagi")
    for v in usr_choice.muutujad:
        variables.append(input(v + " - "))

def main():
    print("Tere!")
    print("See kalkulaator suudab viib valemi õigele kujule kui sisestate vastavad muutujad")
    print("Hetkel toetame vastavaid valemarvutusi:")
    for i, x in enumerate(kõik_valemid):
        print(str(i+1) + ". " + x.nimi + "\n")
    usr_choice = kõik_valemid[int(input("Valige vastav valem: "))-1]
    operation = int(input("Hetkel suudab kalkulaator (1) avaldada muutuja või (2) vastava muutuja välja arvutada, mida teha soovite? "))
    if  operation == 2:
        print(arvuta(usr_choice))
    elif operation == 1:
        print("Valem sisaldab järgmisi muutujadid")
        for i, v in enumerate(usr_choice.muutujad):
            print(str(i+1) + ". " + v)
        avaldatav_muutuja = int(input("Millise muutuja kaudu soovite valemi avaldada? ")) - 1

        print(usr_choice.muutujad[avaldatav_muutuja] + "=" + usr_choice.valemid[avaldatav_muutuja])

main()

