import json
from os import listdir

def get_valemiklassid():
    with open('./valemid/valemiklassid.json', 'w+') as f:
        valemiklassid = list(map(lambda el: el.removesuffix('.json'), listdir('./valemid')))
        valemiklassid.remove('valemiklassid')
        json.dump(valemiklassid, f, indent=4, ensure_ascii=False)
        return valemiklassid

class ValemiKalkulaator:

    # konstruktor loob uue faili nt ValemiKalkulaator("füüsikalised valemid")
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            with open('./valemid/'+file_name+'.json', 'r+') as f:
                try:
                    self.valemid = json.load(f)
                except:
                    self.valemid = {}
                    json.dump(self.valemid, f, indent=4)
        except:
            pass

    # funktsioon teisenda võtab esimeseks argumendiks konkreetse valemi ja teiseks muutuja
    # kiiruse valemi puhul: teisenda("kiiruse arvutamise valem", "v")
    def teisenda(self, valem, väljund):
        return (väljund, self.valemid.get(valem).get(väljund)[0])

    #funktsioon arvuta sisenda on analoogne funktsioon teisenda sisendiga kuid nüüd on kolmandaks sisendiks muutujate väärtused vastavalt selles järjekorras nagu nad valemi sõnastikus esinevad.
    #kiiruse valemi puhul: arvuta("kiiruse arvutamise valem", "v", [10,4])
    def arvuta(self, valem, väljund, väärtused):
        self.valem = self.teisenda(valem, väljund)[1]
        print(self.valem)
        self.i = 0
        for x in self.valemid.get(valem):
            if x != väljund:
                self.valem = self.valem.replace(x, str(väärtused[self.i]))
                self.i += 1
        return (self.valem, eval(self.valem))
    
    # funktsioon lisa_valem lisab sõnastikku valemeid ning võtab ainukeseks argumendiks lisatava sõnastiku
    # nt kiiruse valemi puhul: lisa_valem("kiiruse arvutamise valem":{"s": "v*t","v": "s/t","t": "s/v"}
    def lisa_valem(self, valem):
        try:
            self.valemid.update(valem)
        except:
            self.valemid = valem
        with open('./valemid/'+self.file_name+'.json', 'w+') as f:
            json.dump(self.valemid, f, indent=4, ensure_ascii=False)

    # funktsioon eemalda_valem eemaldab valemeid ning võtab sisendiks vastava valemi nime
    # nt kiiruse valemi puhul: eemalda_valem("kiiruse arvutamise valem")
    def eemalda_valem(self, valem):
        del self.valemid[valem]
        with open('./valemid/'+self.file_name+'.json', 'w+') as f:
            json.dump(self.valemid, f, indent=4, ensure_ascii=False)

    def get_valemid(self):
        return list(self.valemid.keys())

    def get_valem(self, valem):
        return self.valemid.get(valem)
