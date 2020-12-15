import json

with open('ühikute_teisendamise_andmed.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)
    si_prefixes = data.get('si_prefixes')
    tüved = data.get('tüved')


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

#SISEND = sisendühik,väljundühik(nt mm, km, mmA) (kui väljund on tühi "" siis teisendab põhiühikuks
#VÄLJUND = ennik kujul(sisendühiku nimetus, väljendühiku nimetus, kordaja)
# Väljundi näide (('mg', 'milligramm'), ('kg', 'kilogramm'), 1000000)
def unit_cal(unit_in, unit_out):
    try:
        unit_in_parameters = analyse_unit(unit_in)
        if unit_out == "":
            if unit_in_parameters[1][0] == "g":
                unit_out_parameters = analyse_unit("kg")
            else:
                unit_out_parameters = analyse_unit(unit_in_parameters[1][0])
        else:
            unit_out_parameters = analyse_unit(unit_out)
        if unit_in_parameters[1][0] != unit_out_parameters[1][0]:
            raise ValueError("Ühikud on erinevad tüüpi. Sisesta samad ühikud.")
        unit_in_description = (unit_in_parameters[0][0]+unit_in_parameters[1][0], unit_in_parameters[0][1]+unit_in_parameters[1][1])
        unit_out_description = (unit_out_parameters[0][0]+unit_out_parameters[1][0], unit_out_parameters[0][1]+unit_out_parameters[1][1])
        return (unit_in_description, unit_out_description, 10**(unit_out_parameters[0][2]-unit_in_parameters[0][2]))
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

    print("\nSelleks, et saada " + tulemus[0][1] + "ist " + tulemus[1][1] + " peate korrutama arvu " + str(tulemus[2]) + "ga")
