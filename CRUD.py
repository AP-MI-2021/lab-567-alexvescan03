from Domain.vanzare import Vanzare

def addVanzare(lista, id, titlu, gen, pret, tip_reducere):
    '''
    adaugam o vanzare
    :param lista: lista
    :param id: id
    :param titlu: titlu
    :param gen: gen
    :param pret: pret
    :param tip_reducere:tip reducere
    :return: vanzarea
    '''
    vanzare_noua = Vanzare(id, titlu, gen, pret, tip_reducere)
    lista.append(vanzare_noua)

def modificaVanzare(lista, id, titlu_nou, gen_nou, pret_nou, tip_reducere_nou):
    '''
    modifica vanzarea
    :param lista: lista
    :param id: id
    :param titlu_nou: titlu nou
    :param gen_nou: gen
    :param pret_nou: pret
    :param tip_reducere_nou: tip reducere
    :return: lista modificata
    '''
    for vanzare in lista:
        if vanzare.getId() == id:
            vanzare.setTitlu(titlu_nou)
            vanzare.setGen(gen_nou)
            vanzare.setPret(pret_nou)
            vanzare.setTipReducere(tip_reducere_nou)

def stergeVanzare(lista, id):
    '''
    sterge o lista
    :param lista: lista
    :param id: id
    :return:
    '''
    return [ vanzare for vanzare in lista if vanzare.getId() != id]
