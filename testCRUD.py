from Logic.CRUD import addVanzare, stergeVanzare, modificaVanzare


def testAddVanzari():
    vanzari = []
    addVanzare(vanzari, "1", "200 de leghe sub mari", "Fantasy", 100, "gold")
    for vanzare in vanzari:
        if vanzare.getId() == id:
            assert (vanzare.getTitlu() == "200 de leghe sub mari" and vanzare.getGen() == "Fantasy" and vanzare.getPret() == 100 and vanzare.getTipReducere() == "gold"), "Obiectul nu a fost adaugat"


def testDeleteVanzari():
    vanzari = []
    addVanzare(vanzari, "1", "200 de leghe sub mari", "Fantasy", 100, "gold")
    addVanzare(vanzari, "3", "In jurul pamantului in 80 de zile", "Fantasy", 90, "silver")
    addVanzare(vanzari, "2", "Calatorie in centrul pamantului", "Mister", 95, "none")

    deleted_id = 2
    stergeVanzare(vanzari, deleted_id)
    for vanzare in vanzari:
        assert vanzare.getId() != deleted_id, "Obiectul nu a fost sters"


def testmodificaVanzare():
    vanzari = []
    addVanzare(vanzari, "1", "200 de leghe sub mari", "Fantasy", 100, "gold")
    addVanzare(vanzari, "3", "In jurul pamantului in 80 de zile", "Fantasy", 90, "silver")
    addVanzare(vanzari, "2", "Calatorie in centrul pamantului", "Mister", 95, "none")

    id = 2
    titlu = "harap alb"
    gen = "basm"
    pret = 100
    tip_reducere = "gold"
    modificaVanzare(vanzari, id, titlu, gen, pret, tip_reducere)
    for vanzare in vanzari:
        if vanzare.getId() == id:
            assert (vanzare.getTitlu() == titlu and vanzare.getGen() == gen and vanzare.getPret() == pret and vanzare.getTipReducere() == tip_reducere), "Obiectul nu a fost modificat"



