"""
Exceptiile in Python
Ofera un mecanism eficient de identificare si rezolvare a erorilor care apar in timpul executiei unui program.
In limbajul Python exista posibilitatea tratarii exceptiilor prin stabilirea unei cai alternative de continuare
a executiei programului.

Cateva exemple de exceptii:
- ValueError - se intampla cand o functie primeste alt tip de data ca parametru fata de cel asteptat
- AssertionError - cand expresia evaluata de catre assert este falsa
- SyntaxError - cand o sintaxa nu e respectata [exemplu: << while True print("yeah") >> - lipseste : dupa conditia while]
- ZeroDivisionError - cand incercam sa impartim un nr la 0

Tratarea exceptiilor se face cu blocul try - except - else - finally

Forma generala:

        try:
            <cod ce s-ar putea sa produca exceptii in timpul executiei>

        except(cu sau fara tipul erorii specificat, poate fi si except multiplu):
            <cod care se va rula daca prindem eroare>

        else:
            <cod care se executa daca nu au fost erori>

        finally:
            <cod care se executa indiferent daca s-a produs o exceptie sau nu>

# try si except sunt obligatorii
# else si finally sunt optionale
"""

# Exercitiu cu WHILE si try-except-else-finally:
# Sa se scrie un program care citeste N numere de la tastatura si va afisa suma acestora.
# Citirea numerelor se face pana cand numarul citit va fi egal cu 0.
# Datele de intrare sunt numere intregi
# Se vor trata Exceptiile de tip ValueError, adica daca se introduce altceva decat un nr intreg.
# Nota:
# Se va folosi un bloc try-except-else-finally pentru citirea valorii de la tastatura si tratarea erorii
# daca nu se poate converti textul introdus in numar intreg

# try - except - else - finally

suma_numere = 0
caracter_citit = ''

# ### VARIANTA FARA TRTARE DE EXCEPTII AR FI:
# while caracter_citit != 0:
#     caracter_citit = int(input("Introduceti un nr si apasati enter: "))
#     suma_numere += caracter_citit

# ### VARIANTA CU TRTARE DE EXCEPTII:
while caracter_citit != 0:
    try:
        caracter_citit = int(input("Introduceti un numar si apasati enter: "))
    except ValueError:
        print("Ati introdus un alt tip de caracter.")
    else:
        suma_numere += caracter_citit
    finally:
        if caracter_citit != 0:
            print("Continuam.")
        else:
            print(f"Sfarsit. Suma numerelor introduse este {suma_numere}")