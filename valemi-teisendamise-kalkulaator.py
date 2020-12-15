import json

class TeisendusKalkulaator:
    def __init__(self, file_name):
        self.file_name = file_name
        with open('./valemid/'+file_name+'.json', 'a+') as f:
            try:
                self.valemid = json.load(f)
            except:
                self.valemid = {}
                json.dump(self.valemid, f, indent=4)

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
        with open('./valemid/'+self.file_name+'.json', 'w+') as f:
            json.dump(self.valemid, f, indent=4, ensure_ascii=False)

    def eemalda_valem(self, valem):
        del self.valemid[valem]
        with open('./valemid/'+self.file_name+'.json', 'w+') as f:
            json.dump(self.valemid, f, indent=4, ensure_ascii=False)

    def get_valemid(self):
        return self.valemid
