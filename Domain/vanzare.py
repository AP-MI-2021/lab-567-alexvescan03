def creareVanzare(id, titlu, gen, pret, tipReducere):
    '''
    creeaza un dictionar care reprezinta vanzari de  carti
    :param id: str
    :param titlu: str
    :param gen: str
    :param pret: float
    :param tipReducere: str
    :return:un dictionar ce contine o vanzare
    '''
    return[
         id,
        titlu,
         gen,
         pret,
         tipReducere]


def getId(Vanzare):
    '''
    da id-ul unei vanzari
    :param Vanzare:dictionar ce contine o vanzare
    :return:meniul vanzare
    '''
    return Vanzare[0]

def gettitlu(Vanzare):
    '''
    da numele unei vanzari
    :param Vanzare:
    :return:
    '''
    return Vanzare[1]

def getgen(Vanzare):
    return Vanzare[2]

def getpret(Vanzare):
    return Vanzare[3]

def gettipReducere(Vanzare):
    return Vanzare[4]

def toString(Vanzare):
    return "Id: {}, titlu: {}, gen: {}, pret: {}, tipReducere: {}".format(
        getId(Vanzare),
        gettitlu(Vanzare),
        getgen(Vanzare),
        getpret(Vanzare),
        gettipReducere(Vanzare),
    )