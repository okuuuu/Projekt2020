import json
from os import listdir

class ValemiKalkulaator:

    # siin luuakse muutuja valemiklassid mis sisaldab kõiki valemeid mis hetkel salvestatud on
    try:
        with open('./valemid/valemiklassid.json', 'r') as f:
            valemiklassid = json.load(f)
    except:
        with open('./valemid/valemiklassid.json', 'w+') as f:
            valemiklassid = list(map(lambda el: el.removesuffix('.json'), listdir('./valemid')))
            json.dump(valemiklassid, f, indent=4, ensure_ascii=False)


    # konstruktor loob uue faili nt ValemiKalkulaator("füüsikalised valemid")
    def __init__(self, file_name):
        with open('./valemid/valemiklassid.json', 'w+') as f:
            valemiklassid.append(file_name)
            json.dump(valemiklassid, f, indent=4, ensure_ascii=False)
        self.file_name = file_name
        with open('./valemid/'+file_name+'.json', 'a+') as f:
            try:
                self.valemid = json.load(f)
            except:
                self.valemid = {}
                json.dump(self.valemid, f, indent=4)

    # funktsioon teisenda võtab esimeseks argumendiks konkreetse valemi ja teiseks muutuja
    # kiiruse valemi puhul: teisenda("kiiruse arvutamise valem", "v")
    def teisenda(self, valem, väljund):
        return self.valemid.get(valem).get(väljund)

    #funktsioon arvuta sisenda on analoogne funktsioon teisenda sisendiga kuid nüüd on kolmandaks sisendiks muutujate väärtused vastavalt selles järjekorras nagu nad valemi sõnastikus esinevad.
    #kiiruse valemi puhul: arvuta("kiiruse arvutamise valem", "v", [10,4])
    def arvuta(self, valem, väljund, väärtused):
        self.valem = self.teisenda(valem, väljund)
        self.i = 0
        for x in self.valemid.get(valem):
            if x != väljund:
                self.valem = self.valem.replace(x, str(väärtused[self.i]))
                self.i += 1
        return (self.valem, eval(self.valem))
    
    # funktsioon lisa_valem lisab sõnastikku valemeid ning võtab ainukeseks argumendiks lisatava sõnastiku
    # nt kiiruse valemi puhul: lisa_valem("kiiruse arvutamise valem":{"s": "v*t","v": "s/t","t": "s/v"}
    def lisa_valem(self, valem):
        self.valemid.update(valem)
        with open('./valemid/'+self.file_name+'.json', 'w+') as f:
            json.dump(self.valemid, f, indent=4, ensure_ascii=False)

    # funktsioon eemalda_valem eemaldab valemeid ning võtab sisendiks vastava valemi nime
    # nt kiiruse valemi puhul: eemalda_valem("kiiruse arvutamise valem")
    def eemalda_valem(self, valem):
        del self.valemid[valem]
        with open('./valemid/'+self.file_name+'.json', 'w+') as f:
            json.dump(self.valemid, f, indent=4, ensure_ascii=False)

    def get_valemid(self):
        return self.valemid
