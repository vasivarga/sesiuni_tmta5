"""
Structuri repetitive = modalitati prin care putem executa un cod in mod repetat
pana cand o anumita conditie nu mai este indeplinita
sau pana cand nu ne mai incadram intr-un anumit interval

Exista patru tipuri de structuri repetitive:
 - while
 - do while (nu e in scopul cursului)
 - for
 - for each

Modalitati de control al structurilor repetitive:
 - break
 - continue
"""

"""
1. While (trad. engleza: cât timp)
Este o structura repetitiva in care se executa o serie de instructiuni cat timp expresia de evaluat este adevarata
De regula, variabila de control a while-ului se declara in afara acestuia.

Sintaxa generala:

                            while expresie_de_evaluat:
                                instructiune
"""

# Exercitiu 1: Vreau sa afisez pe ecran toate numerele de la 1 la 10
# Observam ca initial variabila c are valoarea 1 si este declarata in afara buclei
# La final, in interiorul buclei avem c += 1 care inseamna c = c + 1
# Practic cu fiecare repetare a buclei, valoarea lu c va creste cu 1
# Putem sa numim variabila c variabila de control, deoarece in functe de valoarea ei bucla se repeta sau nu

c = 1
while c <= 10:
    print(f"Numarul curent este: {c}")
    c += 1

# ITERATIA 1:
# c = 1
# while 1 <= 10 => TRUE => se executa codul din bucla
# Afisam "Numarul curent este 1"
# c = 1 + 1 = 2

# ITERATIA 2:
# c = 2
# # while 2 <= 10 => TRUE => se executa codul din bucla
# Afisam "Numarul curent este 2"
# c = 2 + 1 = 3

# ITERATIA 3:
# c = 3
# while 3 <= 10 => TRUE => se executa codul din bucla
# Afisam "Numarul curent este 3"
# c = 3 + 1 = 4

# ...

# ITERATIA 10:
# c = 10
# while 10 <= 10 => TRUE => se executa codul din bucla
# Afisam "Numarul curent este 10"
# c = 10 + 1 = 11

# ITERATIA 11:
# c = 11
# while 11 <= 10 => FALSE => nu se executa codul din bucla. Se trece la urmatoarele lini ide cod


# DEBUGGING = proces prin care analizam codul pentru a vedea datele din memorie in timp real
# Se poate face debug cu ajutorul breakpoint-urilor.
# Acestea se pun printr-un click langa numarul liniei de cod pt care vrem sa analizam datele
# Pentru debug, programul se va rula cu optiunea "Debug" in loc de "Run"

# Exercitiu 2: Vreau sa-i printez pe ecran pe cei 101 dalmatieni
i = 1
while i <= 101:
    print(f"Dalmatianul curent are numarul: {i}")
    i += 1

# Exercitiu 3: Vreau sa printez suma numerelor de la 1 la 10
# Observam ca e langa variabila j, am declarat si variabila suma, care initial trebuie sa fie egala cu 0
j = 1
suma = 0
while j <= 10:
    suma += j
    j += 1
print(f"Suma numerelor este: {suma}")

# Exercitiu 4: Vreau sa parcurg o lista de elemente si sa printez fiecare element
lista_studenti = ["Ramona", "Catalin", "Laurentiu", "George", "Ionut", "Dorin", "Catalin"]
i = 0
while i < len(lista_studenti):
    print(f"Studentul curent este: {lista_studenti[i]}")
    i += 1

# Exercitiu 5: Vreau sa il inlocuiesc pe Dorin cu Andreea
i = 0
while i < len(lista_studenti):
    if lista_studenti[i] == "Dorin":
        lista_studenti[i] = "Andreea"
    i += 1
print(f"Lista finala dupa ce Dorin a fost inlocuit este: {lista_studenti}")

# Exercitiu 5 - break: Vreau sa il inlocuiesc doar pe PRIMUL Catalin din lista cu Dorin
i = 0
while i < len(lista_studenti):
    if lista_studenti[i] == "Catalin":
        lista_studenti[i] = "Dorin"
        break
    i += 1
print(f"Lista dupa inlocuirea lui Catalin : {lista_studenti}")

# break se foloseste pentru a termina executia restului de iteratii indiferent daca conditia mai este indeplinita sau nu
