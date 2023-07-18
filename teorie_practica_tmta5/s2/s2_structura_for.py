"""
2. For = structura repetitiva care este utilizata atunci cand vrem sa parcurgem o lista
cu scopul de a afisa elementele sau de a le modifica, si respectiv atunci cand vrem
sa executam un set de instructiuni de un numar specific de ori.

Elementele din care este compus un for:
- inceputul structurii repetitive (for)
- variabila de iteratie
- inceputul intervalului de parcurs (optional, default = 0)
- sfarsitul intervalului de parcurs (obligatoriu) - capatul superior nu este luat in considerare
- pasul cu care se parcurge range-ul/intervalul (optional, default = 1)

Forma generala:

    for variabila_de_iteratie in range(inceput, sfarsit, pas):
        <instructiuni>

"""

# Exercițiu 1: Vreau sa parcurg numerele de la 0 la 9 si sa le afisez pe toate:
for i in range(0, 10, 1):
    print(f"Numarul curent este {i}.")
print("-----------------------------------------")

# Echivalent cu for-u lde sus este urmatoarul pentru ca mergem de la inceput pana la sfarsit cu pas de 1:
for i in range(10):
    print(f"Numarul curent (varianta 2) este {i}.")
print("-----------------------------------------")


# Exercițiul 2: Vreau sa parcurg numerele de la 0 la 9 si sa le afisez din doua in doua:
for i in range(0, 10, 2):
    print(f"Numarul curent (cu salt de doi pasi) este {i}.")
print("-----------------------------------------")


# Exercițiu 3: Vreau sa parcurg numerele de la 0 la 10 si sa printez care sunt pare/impare:
for i in range(10):
    if i % 2 == 0:
        print(f'Numarul {i} este par')
    else:
        print(f"Numarul {i} este impar")
print("-----------------------------------------")


# Exercițiu 4: Am o lista de liste.
# Vreau sa afișez fiecare lista in ordine pe cate un rand separat.
# Ma voi folosi de proprietatea "end" a functiei print 
# Aceasta imi permite sa schimb caracterul cu care se sfârșește o afișare in consola (caracterul linie noua => \n)

# nested list- embedded list - lista imbricata - sau matrice
lista_elemente = [
    ["Ana", 25],
    ["Alin", 28],
    ["Petru", 24]
]

# Voi folosi for in for pentru a putea atinge acest obiectiv
# Cand avem for in for, prima data se va executa for-ul cel mai interior.

for i in range(len(lista_elemente)):
    for j in range(len(lista_elemente[i])):
        print(f"{lista_elemente[i][j]} ", end=" ")
    print("")

# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1
print("-----------------------------------------")


# # Exercițiu 5: Vrem sa parcurgem o lista de elemente, sa zicem fructe. Vrem sa printam fiecare fruct pe ecran,
# si daca gasim caise sa le înlocuim cu gutui
lista_fructe = ["mere", "pere", "prune", "caise", "struguri", "caise"]
for i in range(len(lista_fructe)):
    if lista_fructe[i] == "caise":
        lista_fructe[i] = "gutui"
print(f"Lista de fructe de toamna este: {lista_fructe}")
print("-----------------------------------------")


# # Exercițiu 6: Avem o lista de culori. Si vrem sa vindem haine in culorile respective
# cand vine un cumparator vrem sa ii prezentam haine in culorile alese de el
# adica, daca cumparatorul ne spune ca nu ii place culoarea x,
# ii vom exclude de la prezentare hainele in culoarea respectiva

lista_culori_disponibile = ["rosu", "galben", "albastru", "fuchsia", "magenta", "roz", "violet", "maro", "negru",
                            "orange", "verde", "indigo"]

liste_culori_de_exclus = ["rosu", "galben", "roz"]

for i in range(len(lista_culori_disponibile)):
    if lista_culori_disponibile[i] not in liste_culori_de_exclus:
        print(f"Va recomandam haina de culoare {lista_culori_disponibile[i]}")
print("-----------------------------------------")

# SAU

for i in range(len(lista_culori_disponibile)):
    if lista_culori_disponibile[i] in liste_culori_de_exclus:
        continue  # dam skip la restul instructiunilor din for
    print(f"Va recomandam haine in culoarea: {lista_culori_disponibile[i]}")
print("-----------------------------------------")

# continue este o modalitate prin care putem sa sarim peste iteratia curenta
# fara sa iesim din structura repetitiva

"""
Foreach = structura repetitiva care este utila mai ales atunci cand vrem sa stergem elemente dintr-o lista
Diferenta intre for si foreach e ca la for stocam indexul in variabila de iteratie
iar la foreach stocam elementul din lista in variabila de iteratie

Sintaxa: 
            for denumire_element in lista_de_elemente:
                <instructiuni de executat>

"""
# EXEMPLU: DE CE NU E OK SA FOLOSIM FOR SIMPLU CAND STERGEM ELEMENTE:
# lista_animale = ["elefant", "maimuta", "leu", "pantera", "cocos"]
# for i in range(len(lista_animale)):
#     print(f"Indexul curent este: {i}")
#     print(f"Animalul curent este: {lista_animale[i]}")
#     print(f"Lungimea listei este : {len(lista_animale)}")
#     if lista_animale[i] == "maimuta":
#         lista_animale.pop(i)
#
# print(f"Lista dupa eliminarea maimutei este: {lista_animale}")
# print(f"Lungimea listei este: {len(lista_animale)}")

# # de recomandat cand vrem sa modificam elemente sa nu folosim for
# # pentru ca dimensiunea listei nu este calculata in mod dinamic
# # si la un moment dar se va incerca sa se acceseze un element de la un index care nu mai exista
#
# # exemplu de foreach
lista_animale = ["elefant", "maimuta", "leu", "pantera", "cocos"]
for animal in lista_animale:
    print(f"indexul curent este: {lista_animale.index(animal)}")
    print(f"animalul curent este: {animal}")
    print(f"lungimea listei este este: {len(lista_animale)}")
    if animal == "maimuta":
        index = lista_animale.index(animal)
        lista_animale.remove(animal)
    print(f"Animalul curent este: {animal}")

print(f"Lista dupa eliminarea maimutei este: {lista_animale}")
print("-----------------------------------------")

# Exercițiu cu WHILE:
# Sa se scrie un program care citeste N numere de la tastatura si va afisa suma acestora.
# Citirea numerelor se face pana cand numarul citit va fi egal cu 0.
# Datele de intrare sunt numere intregi
# Nota: se va converti fiecare numar citit in numar intreg pentru a putea efectua adunarea

caracter_citit = ''
suma_numere = 0

while caracter_citit != 0:
    caracter_citit = int(input("Introduceti un numar: "))
    suma_numere += caracter_citit

print(f"Suma numerelor citite este {suma_numere}")
print("-----------------------------------------")

# Exercițiu cu WHILE + time:
# Sa se afiseze ora curenta pentru 10 secunde consecutive, cu o pauza de 1 secunda intre fiecare afisare
# Nota: Se va importa modulul <time> si se va folosi functia localtime() din acesta,
# localtime() - functie ce returneaza informatii despre timpul curent (an, luna, zi, ora, minut, secunda, etc)
# pentru a instrui compilatorul sa intrerupa executarea codului pt o secunda, se va folosi instructiunea <time.sleep(1)>

import time

timp_curent = time.localtime()  # creaza o variabila de tip struct_time (ne ajuta sa accesam ora curenta)
print(f'Variabila local_time: {timp_curent}')

print(f'Este ora: {timp_curent.tm_hour}')
print(f'Este minutul: {timp_curent.tm_min}')
print(f'Este secunda: {timp_curent.tm_sec}')

secunde_numarate = 0

while secunde_numarate < 10:
    timp_curent = time.localtime()
    print(f'Este ora {timp_curent.tm_hour}:{timp_curent.tm_min}:{timp_curent.tm_sec}')
    time.sleep(1)
    secunde_numarate += 1
print("-----------------------------------------")

# Exercițiu piramida:
# Se introduce un numar n de la tastatura care va reprezenta inaltimea unei "piramide" de numere
# Sa se afiseze piramida de numere dupa urmatorul pattern:
#
# Pentru n = 3 e va afisa:
#
# 0
# 0 1
# 0 1 2
# 0 1 2 3

n = int(input("Introduceti inaltimea piramidei: "))

for i in range(n + 1):
    for j in range(0, i + 1, 1):
        print(f'{j}', end=" ")  # end = " " instruieste compilatorul sa puna spatiu in loc de rand nou la final de linie
    print('')  # punem linie noua dupa fiecare rand afisat
print("-----------------------------------------")

# Exercițiu *:
# Se introduce un numar n de la tastatura
# In consola se va *
# Sa se afiseze piramida de numere dupa urmatorul pattern:
#
# Pentru n = 5 e va afisa:
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = int(input("Introduceti inaltimea graficului: "))

for i in range(n):
    for j in range(i):
        print('* ', end="")  # end="" instruieste compilatorul sa nu puna rand nou la final de linie
    print('')  # punem linie noua dupa fiecare rand afisat

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')  # punem linie noua dupa fiecare rand afisat



