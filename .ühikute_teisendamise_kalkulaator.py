import json

class ÜhikuKalkulaator:
    def __init__(self):
        with open('ühikute_teisendamise_andmed.json', 'r', encoding='UTF-8') as f:
            self.data = json.load(f)
            self.si_prefixes = self.data.get('si_prefixes')
            self.tüved = self.data.get('tüved')

    def get_si_prefixes(self):
        return self.si_prefixes.keys()

# Väljundi näide (('k', 'kilo', 3), ('g', 'gramm'))
    def analyse_unit(self, unit):
        #EESLIITE PUUDUMISE KORRAL
        if unit in self.tüved:
            self.prefix = ("","",0)

        #DECA KORRAL
        elif unit[0:2] == "da":
            self.prefix = ("da","deca",1)

        #MICRO KORRAL
        elif unit[0:6] == "lambda":
            self.prefix = ("lambda","micro",-6)

        #ÜLEJÄÄNUD JUHUD
        elif unit[0:1] in self.si_prefixes:
            self.prefix = self.si_prefixes.get(unit[0:1]) if unit not in self.tüved else ""

        if unit[len(self.prefix[0]):len(unit)] in self.tüved:
            self.body = self.tüved.get(unit[len(self.prefix[0]):len(unit)])
            return(self.prefix,self.body)

# print(analyse_unit(input("unit in - ")))

#SISEND = sisendühik,väljundühik(nt mm, km, mmA) (kui väljund on tühi "" siis teisendab põhiühikuks
#VÄLJUND = ennik kujul(sisendühiku nimetus, väljendühiku nimetus, kordaja)
# Väljundi näide (('mg', 'milligramm'), ('kg', 'kilogramm'), 1000000)
    def unit_cal(self, unit_in, unit_out):
        try:
            self.unit_in_parameters = self.analyse_unit(unit_in)
            if unit_out == "":
                if self.unit_in_parameters[1][0] == "g":
                    self.unit_out_parameters = self.analyse_unit("kg")
                else:
                    self.unit_out_parameters = self.analyse_unit(self.unit_in_parameters[1][0])
            else:
                self.unit_out_parameters = self.analyse_unit(unit_out)
            if self.unit_in_parameters[1][0] != self.unit_out_parameters[1][0]:
                raise ValueError("Ühikud on erinevad tüüpi. Sisesta samad ühikud.")
            self.unit_in_description = (self.unit_in_parameters[0][0]+self.unit_in_parameters[1][0], self.unit_in_parameters[0][1]+self.unit_in_parameters[1][1])
            self.unit_out_description = (self.unit_out_parameters[0][0]+self.unit_out_parameters[1][0], self.unit_out_parameters[0][1]+self.unit_out_parameters[1][1])
            return (self.unit_in_description, self.unit_out_description, 10**(self.unit_out_parameters[0][2]-self.unit_in_parameters[0][2]))
        except:
            raise ValueError("Selliseid väärtused kalkulaator ei toeta")

def main():
    print("Tere!")
    print("See kalkulaator suudab ühikuid teisendada.")
    print("Toetame kõiki SI-süsteemi eesliiteid ja põhiühikuid")
    if input("Kas soovite eesliiteid näha? (y/n) - ") == "y":
        print(ÜhikuKalkulaator().get_si_prefixes())

    algne_ühik = input("Mis ühikust soovite teisendus teha (nt mm, kg jne.) - ")
    lõpu_ühik = input("Mis ühikuks soovite vastuse saada (nt cm, dg jne.) - ")

    tulemus = ÜhikuKalkulaator().unit_cal(algne_ühik, lõpu_ühik)

    print("\nSelleks, et saada " + tulemus[0][1] + "ist " + tulemus[1][1] + " peate korrutama arvu " + str(tulemus[2]) + "ga")
