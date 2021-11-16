from Domain import vanzare
from Logic.CRUD import *
from Logic.functionalitati import *
import copy

def printMenuUI():
    print("*****************************************************************************************************")
    print("0. Exit")
    print("1. Adauga o vanzare")
    print("2. Modifica o vanzare")
    print("3. Sterge o vanzare")
    print("4. Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold.")
    print("5. Modificarea genului pentru un titlu dat.")
    print("6. Determinarea prețului minim pentru fiecare gen.")
    print("7. Ordonarea vânzărilor crescător după preț.")
    print("8. Afișarea numărului de titluri distincte pentru fiecare gen.")
    print("9. Afisati toate vanzarile")
    print("10. Undo")
    print("*****************************************************************************************************")


def addVanzareUI(lista):
    duplicat = True
    id = input("Introduceti ID:")
    if len(lista) > 0:
        while duplicat == True:
            duplicat = False
            for vanzare in lista:
                if vanzare.getId() == id:
                    print("exista deja acest id")
                    id = input("Introduceti ID:")
                    duplicat = True
    titlu = input("Introduceti Titlu:")
    gen = input("Introduceti Gen:")
    pret = input("Introduceti Pret:")
    pretBun = True
    while pretBun == True:
        pretBun = False
        try:
            pret = int(pret)
        except ValueError as ve:
            print("eroare:{},te rog reincerca".format(ve))
            pret = input("introduceti pret")
            pretBun = True
    pretBun = True
    while pretBun == True:
        pretBun = False
        try:
            if float(pret) < 0:
                print("pretul nu poate fi negativ")
                pret = input("introduceti pret")
                pretBun = True
        except ValueError as er:
            print("eroare:{},te rog reincerca".format(er))
            pret = input("introduceti pret")
            pretBun = True
    pret = float(pret)
    print("tipuri de reducere:")
    print("      1.None ")
    print("      2.Silver ")
    print("      3.Gold ")
    ok = True
    tip_reducere = ""
    while ok == True:
        tip_reducere = input("Introduceti Tip Reducere:")
        if tip_reducere == "1":
            tip_reducere = "None"
            ok = False
        elif tip_reducere == "2":
            tip_reducere = "Silver"
            ok = False
        elif tip_reducere == "3":
            tip_reducere = "Gold"
            ok = False
        else:
            print("nu exista acest tip de reducere")


    addVanzare(lista, id, titlu, gen, pret, tip_reducere)


def modificaVanzareUI(lista):
    id = ""
    idGresit = True
    while idGresit == True:
        id = input("Introduceti ID-ul cartii de modificat:")

        for vanzare in lista:
            if id == vanzare.getId():

                idGresit = False
        if idGresit == True:
            print("nu exista acest id")
    titlu = input("Introduceti Titlu nou:")
    gen = input("Introduceti Gen nou:")
    pret = input("Introduceti Pret nou:")
    pretBun = True
    while pretBun == True:
        pretBun = False
        try:
            pret = int(pret)
        except ValueError as ve:
            print("eroare:{},te rog reincerca".format(ve))
            pret = input("introduceti pret")
            pretBun = True
    pretBun = True
    while pretBun == True:
        pretBun = False
        try:
            if float(pret) < 0:
                print("pretul nu poate fi negativ")
                pret = input("introduceti pret")
                pretBun = True
        except ValueError as er:
            print("eroare:{},te rog reincerca".format(er))
            pret = input("introduceti pret")
            pretBun = True
    pret = float(pret)
    print("tipuri de reducere:")
    print("      1.None ")
    print("      2.Silver ")
    print("      3.Gold ")
    ok = True
    tip_reducere = ""
    while ok == True:
        tip_reducere = input("Introduceti Tip Reducere:")
        if tip_reducere == "1":
            tip_reducere = "None"
            ok = False
        elif tip_reducere == "2":
            tip_reducere = "Silver"
            ok = False
        elif tip_reducere == "3":
            tip_reducere = "Gold"
            ok = False
        else:
            print("nu exista acest tip de reducere")
    modificaVanzare(lista, id, titlu, gen, pret, tip_reducere)

def stergeVanzareUI(lista):
    id = ""
    idbun = False
    while idbun == False:
        id = input("Dati id-ul vanzarii pe care doriti/"                    
        f"sa il stergeti: ")
        for vanzare in lista:
            if  id == vanzare.getId():
                idbun = True
        if idbun == False:
            print("id ul dat nu exista in vanzari")
    return stergeVanzare(lista, id)

def discountReduceriUI(lista):
    discountReduceri(lista)
    showAllUI(lista)

def modificareGenUI(lista):
    titlu = input("Introduceti titlul de modificat:")
    gen = input("Introduceti noul gen:")
    modificareGen(lista, titlu, gen)

def pretMinimUI(lista):
    rezultat = pretMinim(lista)
    for gen in rezultat.keys():
        print("Gen {0}, Pret minim: {1}".format(gen, rezultat[gen]))

def ordonareCrescatorUI(lista):
    ordonareCrescator(lista)

def nrTitluriDistincteUI(lista):
    rezultat = nrTitluriDistincte(lista)
    for gen in rezultat.keys():
        print("Gen {0}, Numar Titluri: {1}".format(gen, rezultat[gen]))

def showAllUI(lista):
    if len(lista) == 0:
        print("Lista de vanzari este goala!")
    for vanzare in lista:
        print(vanzare)

def undo():
    pass

def runConsoleUI():
    vanzari = []
    vanzari_undo = []
    addVanzare(vanzari, "1", "200 de leghe sub mari", "Fantasy", 100, "gold")
    addVanzare(vanzari, "3", "In jurul pamantului in 80 de zile", "Fantasy", 90, "silver")
    addVanzare(vanzari, "2", "Calatorie in centrul pamantului", "Mister", 95, "none")

    while True:
        printMenuUI()
        optiune = int(input("Introduceti otpiunea dorita:"))
        if optiune == 0:
            break
        elif optiune == 1:
            vanzari_undo = copy.deepcopy(vanzari)
            addVanzareUI(vanzari)


        elif optiune == 2:
            vanzari_undo = copy.deepcopy(vanzari)
            modificaVanzareUI(vanzari)
        elif optiune == 3:
            vanzari_undo = copy.deepcopy(vanzari)

            vanzari = stergeVanzareUI(vanzari)

        elif optiune == 4:
            vanzari_undo = copy.deepcopy(vanzari)
            discountReduceriUI(vanzari)
        elif optiune == 5:
            vanzari_undo = copy.deepcopy(vanzari)
            modificareGenUI(vanzari)
        elif optiune == 6:
            pretMinimUI(vanzari)
        elif optiune == 7:
            vanzari_undo = copy.deepcopy(vanzari)
            ordonareCrescatorUI(vanzari)
        elif optiune == 8:
            nrTitluriDistincteUI(vanzari)
        elif optiune == 9:
            showAllUI(vanzari)
        elif optiune == 10:
            vanzari = copy.deepcopy(vanzari_undo)
        else:
            print("Optiune gresita")