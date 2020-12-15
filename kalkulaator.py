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
    :w
