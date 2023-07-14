"""
################# 1. STRING SLICING #################
Slicing = Modalitate prin care putem sa extragem doar anumite parti dintr-un string (subsiruri)
Slicing-ul se poate face pe baza urmatoarelor elemente:
- pozitie de inceput -> implicit va fi 0 - adica de la inceputul stringului
- pozitie de final -> implicit va fi lungimea stringului - adica pana la final
- pas (cate caractere sa se sara) -> implicit va fi 1 - adica se va afisa fiecare caracter
In general in range-ul pe baza caruia se extrage bucata din string nu se ia in considerare capatul de interval
Exemplu:
Daca ii spun sistemul sa extraga toate caracterele de la pozitia 0 la pozitia 5, de fapt va extrage pana la pozitia 4
"""

poezie = "Cobori in jos Luceafar bland"

# Exercitiu 1: vrem sa extragem toate caracterele din string specificand explicit start-ul si end-ul si pasul implicit
print("Exercitiu 1: " + poezie[0:len(poezie)])

# len(poezie) = 28 -> adica cate caractere sunt in string
# in programare toate elementele dintr-o structura ordonata incep de la indexul 0
# de aceea indexul ultimului element se va afla in pozitia cu 1 mai mica decat lungimea stringului
# avand in vedere ca ultimul caracter se afla in pozita cu 1 mai mica decat lungimea stringului,
# desi capatul de interval nu se ia in considerare nu pierdem ultimul element datorita diferentei intre index si lungime

'''
- Index:                 0  1  2  3  4  5 
- Caracater:             C  o  b  o  r  i
'''

# Exercitiu 2: vrem sa extragem toate caracterele din string folosind start si end implicit
print("Exercitiu 2: " + poezie[:])

# Exercitiu 3: vrem sa extragem toate caracterele din string folosind start si end implicit si pas explicit de 2
# (adica printare din 2 in doua caractere)
print("Exercitiu 3: " + poezie[::2])

# Exercitiu 4: vrem sa extragem toate caracterele din string folosind start si end implicit si pas implicit
print("Exercitiu 4: " + poezie[::])

# Exercitiu 5: vrem sa extragem caracterele incepand de la pozitia 0 pana la pozitia 5 inclusiv
print("Exercitiu 5: " + poezie[0:6])

'''
- Index:                 0  1  2  3  4  5  6  7  8
- Caracater:             F  e  b  r  u  a  r  i  e
- Negative index:       -9 -8 -7 -6 -5 -4 -3 -2 -1
'''

# Exercitiu 6: vrem sa extragem ultimele trei caractere de la final
print("Exercitiu 6: " + poezie[-3:])

# Exercitiu 7: vrem sa printam string-ul in sens invers
print("Exercitiu 7: " + poezie[::-1])

"""
################# 2. METODELE STRING ################# 
Pentru a le putea accesa vom scrie numele string-ului urmat de caracterul "."
"""

propozitie = "Cerul este albastru"


# ### 2.1 Căutarea poziției unui subsir in sir

propozitie.find("a")  # va identifica indexul primului caracter a din string
propozitie.find("c")  # va identifica indexul primului caracter c din string
propozitie.find("X")  # daca nu avem caracterul X in sir, se va returna -1, iar programul continua

print(f"Primul caracter 'a' se afla la pozitia {propozitie.find('a')}")
print(f"Primul subsir 'est' se afla la pozitia {propozitie.find('est')}")
print(f"Primul caracter 'c' se afla la pozitia {propozitie.find('c')}")

print(f'Primul caracter "a" se afla in pozitia {propozitie.find("a")}')
print(f'Caracterul "X" se afla in pozitia {propozitie.find("X")}')

# Referinta cod ASCII: https://www.ascii-code.com/


# ### 2.2 Căutarea indexului unui caracter
# va identifica indexul primului caracter C din string
# metoda index face aproape acelasi lucru ca metoda find
# Diferenta intre find si index este ca "find" returneaza -1 in cazul in care caracterul nu e gasit si "index" da eroare

# propozitie.index("C") - va identifica indexul primului caracter C din string
# propozitie.index("X") - daca nu avem caracterul X in sir, se va returna o eroare si programul se opreste

print(f"Primul caracter 'a' se afla la pozitia {propozitie.index('a')}")
# print(f"Primul caracter 'c' se afla la pozitia {propozitie.index('c')}") - eroare - nu gaseste caracterul c

# ### 2.3 - Impartirea șirului intr-o lista de subșiruri

print(propozitie.split())
# Functie care sparge string-ul in functie de cuvintele componente.
# rezultatul este o lista
# separatorul implicit este spatiu, dar se poate suprascrie

print(propozitie.split())  # cu separator implicit(spatiu): returneaza lista ['Cerul', 'este', 'albastru']

propozitie2 = "Hel,lo, wor,ld"
print(propozitie2.split(","))  # # Am suprascris separatorul cu ",": returneaza lista ['Hel', 'lo', ' wor', 'ld']


# ### 2.4 - Upper Case (Litere mari)
print(propozitie.upper())


# ### 2.5 - Lower Case (Litere mici)
print(propozitie.lower())


# ### 2.6 - Înlocuirea/tăierea caracterelor "albe" (whitespaces)
propozitie3 = "   Hello, world   "
print(propozitie3.strip())  # returneaza "Hello, World!" fara caracterele goale de la inceput si sfarsit


# ### 2.7 - Înlocuirea caracterelor specifice cu alte caractere
propozitie4 = "Hello world"
print(propozitie4.replace("Hello", "Bye"))

# ### 2.8 - Numărarea apariției unui subșir într-un șir
propozitie5 = "Hello world"
print(propozitie5.count("o")) # numara de cate ori apare un anumit substring in string-ul de la care plecam
print(propozitie5.count("ll"))

# ### 8 - Verificarea daca un șir are caracterele de tip digit
print(propozitie.isdigit())
text1 = "1"
print(text1.isdigit())
text2 = "1"
print(text2.isnumeric())
text3 = "1"
print(text3.isdecimal())
text1 = "-1"
print(text1.isdigit())
text2 = "-1"
print(text2.isnumeric())
text3 = "-96"
print(text3.isdecimal())

# verifica daca toate caracterele dintr-un string sunt cifre
# atentie!!! sunt trei functii care fac asta: isDigit, isNumeric, isDecimal

# Diferenta intre cele trei metode:
# https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-python






