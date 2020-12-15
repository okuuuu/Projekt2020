import json

class TeisendusKalkulaator:
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            with open('valemid.json', 'r+', encoding='UTF-8') as f:
                self.valemid = json.load(f)
                if file_name not in self.valemid.get('valemid'):
                    self.valemid[self.file_name]={}
                    json.dump(self.valemid, f, indent=4, ensure_ascii=False)
            self.valemid = self.valemid.get('valemid').get(self.file_name)
        except:
            with open('valemid.json', 'w+', encoding='UTF-8') as f:
                json.dump({'valemid':{file_name:{}}}, f, indent=4, ensure_ascii=False)
                self.valemid = {file_name:{file_name:{}}}

        #with open('./'+file_name+'.json', 'a+') as f:
        #    try:
        #        self.valemid = json.load(f.read())
        #    except:
        #        self.valemid = json.load('{}')
        #        json.dump(self.valemid, f, indent=4)

    def teisenda(self, valem, väljund):
        return self.valemid.get(valem).get(väljund)

    def arvuta(self, valem, väljund, väärtused):
        self.valem = self.teisenda(valem, väljund)
        self.i = 0
        for x in self.valemid.get(valem):
            if x != väljund:
                self.valem = self.valem.replace(x, str(väärtused[self.i]))
                self.i += 1
        return (self.valem, eval(self.valem))
    
    def lisa_valem(self, valem):
        self.valemid.update(valem)
        with open('valemid.json', 'r') as f:
            self.entire_file = json.load(f)
        with open('valemid.json', 'w+') as f:
            self.entire_file['valemid'][self.file_name] = self.valemid
            json.dump(self.entire_file, f, indent=4, ensure_ascii=False)

    def eemalda_valem(self, valem):
        with open('valemid.json', 'w+') as f:
            del json.load(f.read())[(self.file_name)][valem]
            json.dump(self.valemid, f, indent=4, ensure_ascii=False)

    def get_valemid(self):
        return self.valemid

füüsikalised_valemid = TeisendusKalkulaator('füüsikalised_valemid')
füüsikalised_valemid.lisa_valem({"kiiruse arvutamise valem":{'s':'v*t','v':'s/t','t':'s/v'}})
füüsikalised_valemid.lisa_valem({"võnkeperioodi arvutamise valem":{'s':'v*t','v':'s/t','t':'s/v'}})
#print(füüsikalised_valemid.arvuta("kiiruse arvutamise valem", "s", [5,3]))
