from tkinter import *
import ühikute_teisendamise_kalkulaator as ük
from valemite_teisendamise_kalkulaator import ValemiKalkulaator as vk

def ühikute_kalkulaator():
        print("Tere!")
        print("See kalkulaator suudab ühikuid teisendada.")
        print("Toetame kõiki SI-süsteemi eesliiteid ja põhiühikuid")
        if input("Kas soovite eesliiteid näha? (y/n) - ") == "y":
            print(ük.si_prefixes.keys())

            algne_ühik = input("Mis ühikust soovite teisendus teha (nt mm, kg jne.) - ")
            lõpu_ühik = input("Mis ühikuks soovite vastuse saada (nt cm, dg jne.) - ")

            tulemus = ük.unit_cal(algne_ühik, lõpu_ühik)

            print("\nSelleks, et saada " + tulemus[0][1] + "ist " + tulemus[1][1] + " peate korrutama arvu " + str(tulemus[2]) + "ga")

def valemite_kalkulaator():
        print("Tere!")
        print("See kalkulaator suudab viib valemi õigele kujule kui sisestate vastavad muutujad")
        print("Hetkel toetame vastavaid kalkulaatoreid:\n")
        supported_calc = vk.valemiklassid

        for i, calc in enumerate(supported_calc):
            print(str(i+1) + ". " + calc)

        if input("Kas soovite näha milliseid valemeid vastavad kalkulaatorid toetavad? (y/n) - ") == "y":
            index = int(input("Palun sisestage indeks: "))
            print(vk(supported_calc[index-1]).get_valemid())

        if input("-- Kas soovite valemeid lisada (y/n) - ") == "y":
                muutujad = {}
                nimi = input("Mis on valemi nimi? ")
                x = int(input("Mitu erinevat muutujat on valemis? "))
                for i in range(x):
                    muutujad[input("Sisesta " + str(i+1) + ". muutuja tähistus: ")] = ""

                print(muutujad)
                print("Kasutades Pythoni syntaxi, kuidas vastavad muutujad avalduvad: " + " ".join(muutujad.keys()))
                for muutuja in muutujad:
                    muutujad[muutuja] = input(muutuja + "= ")
                vk(nimi).lisa_valem({nimi:muutujad})

        if input("-- Kas soovite valemeid eemaldada (y/n) - ") == "y":
            #Näitan kõik kalkulaatorid
            for i, calc in enumerate(supported_calc):
                print(str(i+1) + ". " + calc)
            calc = int(input('Millisest kalkulaatorist?: '))-1

            #Näitan vastava kalkulaatori valemid
            for i, x in enumerate(vk(supported_calc[calc]).get_valemid().keys()):
                print(str(i+1) + ". " + x)
            indeks = int(input('Milline valem?: '))-1

            vk(supported_calc[calc]).eemalda_valem(list(vk(supported_calc[calc]).get_valemid().keys())[indeks])

valemite_kalkulaator()
