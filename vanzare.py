class Vanzare:

    def __init__(self, id, titlu, gen, pret, tip_reducere):
        self.id = id
        self.titlu = titlu
        self.gen = gen
        self.pret = pret
        self.tip_reducere = tip_reducere

    def getId(self):
        return self.id

    def getTitlu(self):
        return self.titlu

    def getPret(self):
        return self.pret

    def getGen(self):
        return self.gen

    def getTipReducere(self):
        return self.tip_reducere

    def setId(self, id_nou):
        self.id = id_nou

    def setTitlu(self, titlu_nou):
        self.titlu = titlu_nou

    def setPret(self, pret_nou):
        self.pret = pret_nou

    def setGen(self, gen_nou):
        self.gen = gen_nou

    def setTipReducere(self, tip_reducere_nou):
        self.tip_reducere = tip_reducere_nou

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return "Vanzare - Id: {0}, Titlu: {1}, Gen:{2}, Pret:{3}, Tip reducere:{4}".format(self.id, self.titlu, self.gen, self.pret, self.tip_reducere)