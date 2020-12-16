from tkinter import *
import re
import ühikute_teisendamise_kalkulaator
import valemite_teisendamise_kalkulaator 

def ühikute_kalkulaator():
        print("Tere!")
        print("See kalkulaator suudab ühikuid teisendada.")
        print("Toetame kõiki SI-süsteemi eesliiteid ja põhiühikuid")
        if input("Kas soovite eesliiteid näha? (y/n) - ") == "y":
            print(ühikute_teisendamise_kalkulaator.si_prefixes.keys())

            algne_ühik = input("Mis ühikust soovite teisendus teha (nt mm, kg jne.) - ")
            lõpu_ühik = input("Mis ühikuks soovite vastuse saada (nt cm, dg jne.) - ")

            tulemus = ühikute_teisendamise_kalkulaator.unit_cal(algne_ühik, lõpu_ühik)

            print("\nSelleks, et saada " + tulemus[0][1] + "ist " + tulemus[1][1] + " peate korrutama arvu " + str(tulemus[2]) + "ga")

def kalkulaator():
        def print_kalkulaatorid(toetatud_kalkulaatorid):
            for i, x in enumerate(toetatud_kalkulaatorid):
                kalkulaator = valemite_teisendamise_kalkulaator.ValemiKalkulaator(x)
                print(str(i+1) + ". " + x)
                for vi, valem in enumerate(kalkulaator.get_valemid()):
                    print("\t" + str(i+1) + "." + str(vi+1) + ". " + valem)

        print("Tere!")
        print("See kalkulaator suudab viib valemi õigele kujule kui sisestate vastavad muutujad")
        print("Hetkel toetame vastavaid kalkulaatoreid:\n")

        toetatud_kalkulaatorid =  valemite_teisendamise_kalkulaator.get_valemiklassid()
        print_kalkulaatorid(toetatud_kalkulaatorid)

        kalkulaatori_indeks = int(input("Mis kalkulaatorid soovite kasutada? (sisesta indeks) - "))-1
        kalkulaator = valemite_teisendamise_kalkulaator.ValemiKalkulaator(toetatud_kalkulaatorid[kalkulaatori_indeks])
        kalkulaatori_valemid = kalkulaator.get_valemid()

        def valemite_lisamine():
                muutujad = {}
                nimi = input("Mis on valemi nimi? ")
                x = int(input("Mitu erinevat muutujat on valemis? "))
                for i in range(x):
                    muutujad[input("Sisesta " + str(i+1) + ". muutuja tähistus: ")] = []

                print("Kasutades Pythoni syntaxi, kuidas vastavad muutujad avalduvad: " + " ".join(muutujad.keys()))
                for muutuja in muutujad:
                    muutujad[muutuja].append(str(input(muutuja + "= ")))

                print("Mis on muutujate si-põhiühikud?")
                for muutuja in muutujad:
                    si_ühik = input(muutuja + "= ")
                    muutujad[muutuja].append(si_ühik)

                kalkulaator.lisa_valem({nimi:muutujad})

        def valemite_eemaldamine():
        #if input("-- Kas soovite valemeid eemaldada (y/n) - ") == "y":
            for i, valem in enumerate(kalkulaatori_valemid):
                print("\t" + str(i+1) + ". " + valem)

            eemaldatav_valem = kalkulaatori_valemid[int(input('Milline valem?: '))-1]
            kalkulaator.eemalda_valem(eemaldatav_valem)

        def arvuta():
            valemi_indeks = int(input('Milline valem?: ' + str(kalkulaatori_indeks+1) + "."))-1
            valemi_nimi = kalkulaatori_valemid[valemi_indeks]
            valem = kalkulaator.get_valem(valemi_nimi)

            muutujad = list(kalkulaator.get_valem(valemi_nimi).keys())
            print("\tMuutujad: " + ",".join(muutujad))
            muutuja = input('Milline muutuja? - ')

            if input("-- Kas soovite arvutada konkreetsete muutuja väärtustega (y/n) - ") == "y":
                muutujate_väärtused = []
                muutujad.remove(muutuja)
                for x in muutujad:
                    muutuja_väärtus = input(x + "= ")
                    match = re.search('\D*$',muutuja_väärtus)
                    if match:
                        ühik = match.group()
                        kordaja = ühikute_teisendamise_kalkulaator.unit_cal(ühik, "")[2]
                        muutuja_väärtus_põhiühikutes = kordaja * float(muutuja_väärtus.removesuffix(ühik))
                    muutujate_väärtused.append(float(muutuja_väärtus_põhiühikutes))

                arvuta = kalkulaator.arvuta(valemi_nimi, muutuja, muutujate_väärtused)

                tulemuse_ühik = str(valem.get(muutuja)[1]) if match else ""

                print(muutuja + "= " + arvuta[0] +  "= " + str(arvuta[1]) + tulemuse_ühik)
            else:
                teisenda =  kalkulaator.teisenda(valemi_nimi, muutuja)
                print(teisenda[0] + "= " + teisenda[1])

        function_dict = {'valemite lisamine':valemite_lisamine,
                         'valemite_eemaldamine':valemite_eemaldamine,
                         'teisendamine/arvutamine':arvuta}

        for i, x in enumerate(function_dict):
            print(str(i+1) + ". " + x)

        function_dict[list(function_dict.keys())[int(input("Sisesta operatsiooni indeks "))-1]]()
kalkulaator()
