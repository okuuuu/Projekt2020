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

def main():
    print("Tere!")
    print("See kalkulaator suudab viib valemi õigele kujule kui sisestate vastavad muutujad")
    print("Hetkel toetame vastavaid valemarvutusi:\n")
    for i, x in enumerate(kõik_valemid):
        print(str(i+1) + ". " + x.nimi + " " + x.muutujad[0] + "=" + x.valemid[0])
    usr_valem = kõik_valemid[int(input("\nValige vastav valem: "))-1]
    usr_var = usr_valem.muutujad.index(input("Millise muutuja kaudu soovite valemi avaldada? "))

    operation = True if int(input("\nKuvan lihtsalt valemi = 1\nArvutan kindlate väärtustega = 2\n\nValik: ")) == 2 else False

    opereeri(usr_valem, usr_var, operation)

main()

