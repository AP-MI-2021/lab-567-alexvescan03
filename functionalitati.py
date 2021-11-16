def discountReduceri(lista):
    for vanzare in lista:
        if vanzare.getTipReducere() == "silver":
            vanzare.setPret(95/100*vanzare.getPret())
        elif vanzare.getTipReducere() == "gold":
            vanzare.setPret(90/100*vanzare.getPret())

def modificareGen(lista, titlu, gen):
    for vanzare in lista:
        if vanzare.getTitlu() == titlu:
            vanzare.setGen(gen)

def pretMinim(lista):
    pretMinimPerGen = {}
    for vanzare in lista:
        if vanzare.getGen() in pretMinimPerGen.keys():
            if vanzare.getPret() < pretMinimPerGen[vanzare.getGen()]:
                pretMinimPerGen[vanzare.getGen()] = vanzare.getPret()
        else:
            pretMinimPerGen[vanzare.getGen()] = vanzare.getPret()
    return pretMinimPerGen

def ordonareCrescator(lista):
    lista.sort(key= lambda x: x.getPret() )

def nrTitluriDistincte(lista):
    titluriPerGen = {}
    for vanzare in lista:
        if vanzare.getGen() in titluriPerGen.keys():
            titluriPerGen[vanzare.getGen()] = titluriPerGen[vanzare.getGen()] + 1
        else:
            titluriPerGen[vanzare.getGen()] = 1
    return titluriPerGen