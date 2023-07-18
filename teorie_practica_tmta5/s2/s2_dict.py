"""
Dictionare in python

Un dictionar este o structura de date ordonata care contine mai multe perechi cheie: valoare
Cheile trebuie sa fie unice. Ele servesc drept inlocuitor pentru indexul de la liste
Operatii care se pot face intr-un dictionar:
- adaugare perechi
- stergere perechi
- modificare valoare cheie
- accesare elemente
"""

# 1. Creare dictionar gol:
# varianta 1
dict_gol = {}
print(dict_gol)

# varianta 2
dict_gol = dict()
print(dict_gol)

# 2. Creare dictionar populat:
masina = {
    "nume": "bmw",
    "model": "X5",
    "an_fabricatie": 2020,
    "tip_tractiune": "4x4",
    "norme_euro": "euro6",
    "combustibil": "diesel"
}

# 3. Accesarea elementelor dintr-un dictionar.
# Varianta 1 - cu sintaxa: nume_dict["cheie"]
print(f"Numele masinii este: {masina['nume']}")

# Varianta 2 - cu sintaxa: nume_dict.get("cheie")
print(f"Modelul masinii este: {masina.get('model')}")

# 4. Adaugarea elementelor in dictionar
# Sintaxa: nume_dict["proprietate_noua"] = valoare
masina["numar_locuri"] = 5
print(f"Masina are  {masina['numar_locuri']} locuri")

# 5.Actualizarea elementelor din dictionar
#varianta 1
masina.update({"norme_euro": "euro6"})
print(f"Norma europeana curenta este: {masina['norme_euro']}")

#varianta 2
masina["an_fabricatie"] = 2012
print(f"Am corectat anul de fabricatie al masinii la valoarea {masina['an_fabricatie']}")

# 6.Stergerea elementelor din dictionar
masina.pop("nume")
print(f"Dictionarul curent este {masina}")

# 7. Accesarea cheilor din dictionar
print(f"Proprietatile masinii mele sunt: {masina.keys()}")

# 8. Accesarea valorilor din dictionar:
print(f"Valorile proprietatilor masinii mele sunt: {masina.values()}")

# 9. Accesarea perechilor cheie: valoare
print(f"Dictionarul este format din urmatoarele perechi de cheie:valoare: {masina.items()}")

# 10. Dictionar imbricat
sucuri = {
    "pepsi": {
        "nume": "Pepsi",
        "producator": "Pepsi SRL",
        "cantitate_vanzare": "500ml",
        "impachetare": "baxuri"
    },
    "cola": {
        "nume": "Coke SRL",
        "cantitate_vanzare": "2l",
        "impachetare": "sticla"
    },
    "fanta":
        {
            "nume": "fanta",
            "producator": "Fanta Co",
            "impachetare": "bax",
            "promovare":
                {
                    "reclama": "Suc cu spirit tanar!"
                },
            "televiziune promovare": ["tvr1", "tvr2", "acasa tv", "antena1"]
        }
}
print(sucuri["pepsi"]["impachetare"])
print(sucuri["fanta"]["promovare"]["reclama"])
print(sucuri["fanta"]["televiziune promovare"][2])