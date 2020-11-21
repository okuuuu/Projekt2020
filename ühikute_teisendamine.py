si_prefixes = {
        "Y":("Y","yotta",24),
        "Z":("Z","zetta",21),
        "E":("E","exa",18),
        "P":("P","peta",15),
        "T":("T","tera",12),
        "G":("G","giga",9),
        "M":("M","mega",6),
        "k":("k","kilo",3),
        "h":("h","hecto",2),
        "da":("da","deca",1),
        "d":("d","deci",-1),
        "c":("c","centi",-2),
        "m":("m","milli",-3),
        "lambda":("lambda","micro",-6),
        "n":("n","nano",-9),
        "p":("p","pico",-12),
        "f":("f","femto",-15),
        "a":("a","atto",-18),
        "z":("z","zepto",-21),
        "y":("y","yocto",-24)}

tüved = {
        "s":("s","sekund"),
        "m":("m","meeter"),
        "g":("g","gramm"),
        "A":("A","amper"),
        "K":("K","kelvin"),
        "mol":("mol","mool"),
        "cd":("cd","kandela")}

# Väljundi näide (('k', 'kilo', 3), ('g', 'gramm'))
def analyse_unit(unit):
    #EESLIITE PUUDUMISE KORRAL
    if unit in tüved:
        prefix = ("","",0)

    #DECA KORRAL
    elif unit[0:2] == "da":
        prefix = ("da","deca",1)

    #MICRO KORRAL
    elif unit[0:6] == "lambda":
        prefix = ("lambda","micro",-6)

    #ÜLEJÄÄNUD JUHUD
    elif unit[0:1] in si_prefixes:
        prefix = si_prefixes.get(unit[0:1]) if unit not in tüved else ""

    if unit[len(prefix[0]):len(unit)] in tüved:
        body = tüved.get(unit[len(prefix[0]):len(unit)])
        return(prefix,body)

# print(analyse_unit(input("unit in - ")))

#SISEND = sisendühik,väljundühik(nt mm, km, mmA), VÄLJUND = ennik kujul(sisendühiku nimetus, väljendühiku nimetus, kordaja)
def unit_cal(unit_in, unit_out):
    try:
        unit_in_parameters = analyse_unit(unit_in)
        unit_out_parameters = analyse_unit(unit_out)
        if unit_in_parameters[1][0] != unit_out_parameters[1][0]:
            raise ValueError("Ühikud on erinevad tüüpi. Sisesta samad ühikud.")
        return (unit_in_parameters[0][1]+unit_in_parameters[1][1], unit_out_parameters[0][1]+unit_out_parameters[1][1], 10**(unit_out_parameters[0][2]-unit_in_parameters[0][2]))
    except:
        raise ValueError("Selliseid väärtused kalkulaator ei toeta")

def main():
    print("Tere!")
    print("See kalkulaator suudab ühikuid teisendada.")
    print("Toetame kõiki SI-süsteemi eesliiteid ja põhiühikuid")
    if input("Kas soovite eesliiteid näha? (y/n) - ") == "y":
        print(si_prefixes.keys())

    algne_ühik = input("Mis ühikust soovite teisendus teha (nt mm, kg jne.) - ")
    lõpu_ühik = input("Mis ühikuks soovite vastuse saada (nt cm, dg jne.) - ")

    tulemus = unit_cal(algne_ühik, lõpu_ühik)

    print("\nSelleks, et saada " + tulemus[0] + "ist " + tulemus[1] + " peate korrutama arvu " + str(tulemus[2]) + "ga")

main()
