from Domain.vanzare import getpret, getgen
from Logic.CRUD import adaugaVanzare
from Logic.Functionalitati import aplicareDiscount, modificareGen, pretMinimGen, ordonareCrescatoarePret, \
    afisareNrTitluriDistincteGen


def testAplicarediscount():
    lista = []
    lista = adaugaVanzare("1","Harap-Alb","Basm",100,"Silver",lista)
    lista = adaugaVanzare("1", "Baltagul", "Roman", 50, "Gold",lista)

    lista =  aplicareDiscount(lista)
    assert len(lista) == 2
    assert getpret(lista[0]) == 95
    assert getpret(lista[1]) == 45

def testModificareGen():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("1", "Baltagul", "Roman", 50, "Gold", lista)

    lista = modificareGen(lista,"Harap-Alb","Fabula")
    assert len(lista) == 2
    assert getgen(lista[0]) == "Fabula"
    assert getgen(lista[1]) == "Roman"

def testPretMinimGen():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("1", "Baltagul", "Basm", 50, "Gold", lista)

    min_p = pretMinimGen(lista,"Basm")
    assert len(lista) == 2
    assert min_p == 50

def testOrdonareCrescatorPret():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("1", "Baltagul", "Basm", 50, "Gold", lista)

    lista = ordonareCrescatoarePret(lista)
    assert len(lista) == 2
    assert getpret(lista[0]) == 50
    assert getpret(lista[1]) == 100

def testNrTitluriDistincteGen():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("1", "Baltagul", "Basm", 50, "Gold", lista)
    lista = adaugaVanzare("1", "Ion","Roman",200,"None",lista)

    nrt = afisareNrTitluriDistincteGen(lista)
    assert len(lista) == 3
    assert nrt["Basm"] == 2
    assert nrt["Roman"] == 1