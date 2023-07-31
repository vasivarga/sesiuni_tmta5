# 1. Declarati o lista cu elemente multitype

lista = ["Ana", "Anton", 2, 45.6, True]  # se acceseaza pe baza de index
print(lista)  # accepta elemente duplicate
# se poate modifica structura (adauga si sterge elemente)


# 2. Declarati o lista goala

lista_goala = list()

"""
set = set()
print(type(set))
dictionar = dict()
print(type(dictionar))
"""


# 3. Accesati orice element din lista pe baza de index

lista = ["Ana", "Anton", 2, 45.6, True]
print(lista[2])


# 4. Accesati pozitia unui element din lista pe baza functiei index()
print(lista.index("Anton"))


# 5. Adaugati elemente in lista atat cu functia append() cat si cu functia insert(). Observati rezultatele
lista.append("cascaval")
print(lista)
lista.insert(1, "Marcel")
print(lista)

# 6. Stergeti elemente din lista atat cu functia pop() cat si cu functia remove(). Observati rezultatele
lista.pop()
print(lista)
lista.remove("Marcel")
print(lista)

# 7. Numarati elementele dintr-o lista folosind functia len()
print(f"Lista are {len(lista)} elemente")


# 8. Numarati de cate ori apare un anumit element in lista folosind functia count()

print(lista.count("Ana"))
lista.append("Ana")
print(lista.count("Ana"))
lista.pop()

# 9. Uniti doua liste folosind functia extend()
lista2 = [1, 4, 6]
# lista = lista + lista2
# lista2 = lista + lista2
print(lista2)
# lista3 = lista + lista2
# lista3V2 = lista.extend(lista2)  NO BUENO
# print(lista3)
lista.extend(lista2)
print(lista)
# print(f'lista extinsa {lista.extend(lista2)}')  NO BUENO


# 10. Sortati lista folosind functia sort()
lista_mea = [3, 5, 9, 7]
lista_mea.sort()
print(lista_mea)

# 11. Inversati continutul listei folosind functia reverse()
lista_mea.reverse()
print(lista_mea)

# 12. Stergeti toate elementele din lista folosind functia clear()
lista.clear()
print(lista)

# 13. Parcurgeti o lista si printati toate elementele din aceasta folosind pe rand for, while si foreach

# for stim numarul de pasi, ai o limita

for i in range(0, len(lista_mea)):
    print(lista_mea[i])

print("#############################")
# while   merge pana o conditie este indeplinita (nu stim numarul de pasi)
i = 0
while i < len(lista_mea):
    print(lista_mea[i])
    i = i + 1
print("#############################")

# for "each"

for element in lista_mea:
    print(element)

print("#############################")

# Bonus 1: Sortati o lista folosind algoritmul de sortare prin metoda bulelor
bule = [9, 5, 6, 1, 2, 13, 29, 17, 36, 0]
switch = ""
j = 1
while j < len(bule):
    for i in range(0, len(bule)-1):
        if bule[i] > bule[i+1]:         # daca 9 (pozitia 0) > 5 (pozitia 1)
            switch = bule[i]            #switch = 9 (pozitia 0)  -> actual pozitia 0 = null
            bule[i] = bule[i+1]         #pozitia 0 = 5 (pozitia 1)  -> actual pozitia 1  devine null
            bule[i+1] = switch          #pozitia 1 = 9 (switch)
    j = j + 1
print(bule)
#bule = [5, 6, 1, 2, 9, 13, 17, 29, 0, 36]  # nu este sorata complet mai trebuie iterat cel putin o data

#bule = [9, 5, 6, 1, 2, 13, 29, 17, 36, 0]  #index 0
        # [5 9 6 1 2 13 29 17 36 0]  #index 1
        # [5 6 9 1 2 13 29 17 36 0]  #index 2
        # [5 6 1 9 2 13 29 17 36 0] #index 3
        # [5 9 1 2 9 13 29 17 36 0] #index 4
        # [5 9 1 2 9 13 29 17 36 0]  #index 5
        # [5 9 1 2 9 13 29 17 36 0]   #index 6
        # [5 9 1 2 3 13 17 29 36 0]   #index 7
        # [5 9 1 2 3 13 17 29 36 0]      #index 8
        # [5 9 1 2 3 13 17 29 0 36] #index 9
        # [5 9 1 2 3 13 17 29 0 36] finala
# for i in range(0, len(bule)-1):
#     if bule[i] > bule[i+1]:         # daca 9 (pozitia 0) > 5 (pozitia 1)
#         switch = bule[i]            #switch = 9 (pozitia 0)  -> actual pozitia 0 = null
#         bule[i] = bule[i+1]         #pozitia 0 = 5 (pozitia 1)  -> actual pozitia 1  devine null
#         bule[i+1] = switch          #pozitia 1 = 9 (switch)
#
# print(bule)

#
#
#
#
#
# # Bonus 2: Incercati sa printati pe ecran pe cei 101 dalmatieni.
# La fiecare dalmatian veti printa pe ecran urmatorul text:
# “Dalmatianul curent se afla in pozitia “i””.
# Atentie, ghilimelele vor trebui tratate folosind caracterul escape

i = 1
while i <= 101:
    print(f'Dalmatianul curent se afla in pozitia \"{i}\"')
    i = i + 1


# 1. Declarati un tuplu        # are structura fixa si ca numar si ca valoare
# se poate accesa prin index
tuplu = (5, 6, 10, 7)

# 2. Declarati un tuplu gol
tuplu_gol = tuple()

# 3. Accesati orice element din tuplu pe baza de index
print(tuplu[2])

# 4. Accesati pozitia unui element din lista pe baza functiei index()
print(tuplu.index(5))

# 5. Folositi functia count() pentru a numara de cate ori apare un element in tuplu
print(tuplu.count(6))

# 6. Folositi functia index() pentru a verifica pozitia la care se afla un
# anumit element in tuplu.
print(tuplu.index(7))

# 7. Incercati sa modificati un element din tuplu si observati rezultatele
# tuplu.remove(10)
# tuplu.append(15)


# 1. Declarati un set

setul_meu = {1, 4, 7, 2, 5}  # nu accepta duplicate
print(setul_meu)  # accesare nu se print index
# poate fi modificat
# 2. Declarati un set gol
set_gol = set()

# 3. Adaugati un element nou in set folosind functia add()
setul_meu.add(12)
print(setul_meu)
setul_meu.add(0)
print(setul_meu)

# 4. Stergeti un element din set folosind functia pop() si respectiv functia remove(). Observati rezultatele
setul_meu.pop()
print(setul_meu)
setul_meu.remove(5)
print(setul_meu)

# 5. Verificati daca un set este o subdiviziune a unui alt set (subset)
set_2 = {2, 4}
if set_2.issubset(setul_meu):
    print("este subset")

# 6. Verificati daca un set contine toate elementele dintr-un alt set + alte elemente (superset)

if setul_meu.issuperset(set_2):
    print("este supraset")

# 7. Verificati care sunt elementele comune intre doua seturi (intersection)

print(setul_meu.intersection(set_2))
print(set_2.intersection(setul_meu))

# 8. Verificati diferenta intre doua seturi cu functia difference()
print(setul_meu.difference(set_2))

# 9. Stergeti toate elementele dintr-un set folosind functia clear()
setul_meu.clear()
print(setul_meu)


# 1. Declarati un dictionar       # functioneaza pe principiul cheie: valoare
dictionarul_meu = {  # key este unica
    "elev": "premiant",  # value poate avea duplicate
    "nota": 9.50,
    "promovat": True,
}
print(dictionarul_meu)

# 2. Declarati un dictionar gol
dict_gol = dict()

# 3. Adaugati un element nou in dictionar folosind functia update()
# si respectiv pe baza de cheie
element_nou = {"tip_examen": "BAC"}
dictionarul_meu.update(element_nou)  # adaugare element cu functia update()
print(dictionarul_meu)
dictionarul_meu.update({"elev": "olimpic"})
print(dictionarul_meu)
dictionarul_meu.update(element_nou)
print(dictionarul_meu)
dictionarul_meu.update({"varsta": "18 ani"})
print(dictionarul_meu)
dictionarul_meu["nume"] = "Tutuca Petre"  # adaugare pe baza de cheie
print(dictionarul_meu)


# 4. Extrageti un element din dictionar folosind metoda get() si respectiv pe baza de cheie
print(dictionarul_meu.get("nume"))
print(dictionarul_meu["nume"])

# 5. Stergeti un element din dictionar folosind functia pop() si respectiv functia popitem().
# Observati rezultatele
dictionarul_meu.pop("tip_examen")
print(dictionarul_meu)
dictionarul_meu.popitem()
print(dictionarul_meu)

# 6. Extrageti pe rand toate cheile, apoi toate valorile, si apoi toate item-urile
# din dictionar
print(f"keys: {dictionarul_meu.keys()}")
print(f"values: {dictionarul_meu.values()}")
print(f"perechi: {dictionarul_meu.items()}")


# 7. Stergeti toate valorile din dictionar folosind metoda clear()
dictionarul_meu.clear()
print(dictionarul_meu)

print("#############################################")

fotbalisti_pe_echipe = {
    "Barcelona": {
        "Dica": {
            "Nume complet": "Nicolae Dica",
            "Varsta": 45,
            "Numar Tricou": 10
        },
        "Banel": {
            "Nume complet": "Banel Nicolita",
            "Varsta": 47,
            "Numar Tricou": 3
        },
        "Dukadam": {
            "Nume complet": "Helmut Dukadam",
            "Varsta": 65,
            "Numar Tricou": 7
        },
    },
    "Real-Madrid": {
        "mutu": {
            "Nume complet": "mutu",
            "Varsta": 45,
            "Numar Tricou": 10
        },
        "radoi": {
            "Nume complet": "radoi",
            "Varsta": 47,
            "Numar Tricou": 3
        },
        "chivu": {
            "Nume complet": "chivu",
            "Varsta": 65,
            "Numar Tricou": 7
        },
        "marian": {
            "Nume complet": "marian",
            "Varsta": 65,
            "Numar Tricou": 7,
            "accidentat": True,
        },
    }
}
#Printati pe ecran numarul de pe tricou al oricarui jucator doriti
print(fotbalisti_pe_echipe["Barcelona"]["Banel"]["Numar Tricou"])

#Folositi functia pop pentru a scoate orice jucator din dictionar
#fotbalisti_pe_echipe["Barcelona"].pop("Banel")
#print(fotbalisti_pe_echipe)
''''
fotbalisti_pe_echipe = {
    "Barcelona": {
        "Dica": "nume",
        "Banel": "nume",
        "Dukadam": "nume"},
    "Real Madrid": {
            "radoi": "nume",
            "mutu": "nume",
            "chivu": "nume"}
}'''

#Printati pe ecran detaliile despre fiecare jucator astfel incat sa obtineti urmatorul rezultat:


'''
La echipa Barcelona joaca jucatorul:
Detalii jucator - Nume Complet: Nicolae Dica, Detalii jucator - Varsta:45, Detalii jucator - Numar Tricou:10

La echipa Barcelona joaca jucatorul:
Detalii jucator - Nume Complet: Banel Nicolita, Detalii jucator - Varsta:47, Detalii jucator - Numar Tricou:

La echipa Barcelona joaca jucatorul:
Detalii jucator - Nume Complet: Dukadam, Detalii jucator - Varsta:45, Detalii jucator - Numar Tricou:7

'''
#for element in list_of_elements  for each

for key, value in fotbalisti_pe_echipe.items():  #aici accesam echipele (cheia Barcelona...Valoare jucatorii( dica banel dukadam)
#barcelona, jucatorii
    for key_interioara, value_interioara in value.items():
        print(f'La echipa {key} joaca jucatorul: ')
        for key_jucator, value_jucator in value_interioara.items():
            print("Detalii jucator ", f' {key_jucator}:{value_jucator}', sep = "-", end=", ")
            # end= incheie fiecare iteratie cu elementul dorit
        print("\n")       #punem un rand gol (Enter in Word)

