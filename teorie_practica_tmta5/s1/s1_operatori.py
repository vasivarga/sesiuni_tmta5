"""
Operatori
Operatorii sunt elemente prin intermediul carora putem efectua operatii asupra variabilelor
Exista patru tipuri de operatori:
- Operatori aritmetici -> prin intermediul carora putem efectua operatii matematice
- Operatori de comparatie -> prin intermediul carora putem efectua comparatii intre continutul variabilelor
- Operatori de atribuire -> prin intermediul carora putem sa alocam valori variabilelor
- Operatori logici -> prin intermediul carora putem evalua conditii mai complexe
alocare = salvare de informatii la adresa de memorie care este identificata de numele variabilei
"""

# 1. OPERATORI ARITMETICI: +, -, *, /, **, %, //
# 1.1. Operatorul + (PLUS)
# Este folosit pentru a aduna doua numere sau pentru a concatena doua string-uri
# Exemple:
nr_1 = 5
nr_2 = 7

str_1 = "ana "
str_2 = "are mere"

# Suma
print(f"Suma celor doua numere este: {nr_1 + nr_2}")

# Concatenare - varianta cu formatare de string
print(f"String-urile concatenate sunt: {str_1 + str_2}")

# Concatenare - varianta fara formatare de string
print("String-urile concatenate sunt: " + str_1 + " " + str_2)

# 1.2. Operatorul - (MINUS)
# Este folosit pentru a efectua diferenta intre doua numere
print(f"Diferenta intre cele doua numere este: {nr_1 - nr_2}")

# 1.3. Operatorul *
# Pentru valori numerice, operatorul "*" reprezintă înmulțirea.
# În cazul unor operanzi de tip str, acesta are rolul de a multiplica valoarea (textul).
print(f"Produsul celor doua numere este: {nr_1 * nr_2}")

# 1.4. Operatorul / este folosit pentru a efectua impartirea a doua numere
print(f"Impartirea celor doua numere a rezultat in numarul: {nr_1 / nr_2}")
# ATENTIE!! rezultatul operatiei efectuate cu operatorul division este float

# 1.5. Operatorul // (FLOOR DIVISION) este folosit pentru a efectua impartirea intreaga a doua numere
# (adica se taie zecimalele de la rezultat)
print(f"Impartirea cu floor division celor doua numere a rezultat in numarul: {nr_1 // nr_2}")
print(f"Impartirea cu celor doua numere a rezultat in urma rotunjirii in numarul: " + str(round(nr_1 / nr_2)))

# 1.6. Operatorul % (MODULO) este folosit pentru a obtine restul impartirii celor doua numere
print(f"Restul impartirii lui {nr_2} la {nr_1} este {nr_2 % nr_1}")

# 1.7. Operatorul ** (RIDICARE LA PUTERE) este folosit pentru a ridica un numar la puterea x
print(f"Numarul {nr_2} ridicat la puterea {nr_1} este {nr_2 ** nr_1}")

# 2. OPERATORI DE COMPARATIE: ==, <=, >=, <, >, !=
# 2.1. OPERATORUL == este folosit pentru a compara doua valori (sau expresii)

# Expresiile sunt combinatii intre variabile, valori si operatori #Ex1: 1+1, #Ex2: a + b = 6
# ATENTIE!!! Nu confundati operatorul de comparatie == cu operatorul de atribuire =
# Rezultatul comparatiei o sa fie boolean

print(f"Cele doua numere sunt egale? {nr_1 == nr_2}")

# 2.2. OPERATORUL <= este folosit pentru a verifica daca primul operand este mai mic sau egal cu al doilea
print(f"Numarul 1 este mai mic sau egal cu numarul 2? {nr_1 <= nr_2}")

# 2.2. OPERATORUL >= este folosit pentru a verifica daca primul operand este mai mare sau egal cu al doilea
print(f"Numarul 1 este mai mare sau egal cu numarul 2? {nr_1 >= nr_2}")

# 2.3. OPERATORUL < este folosit pentru a verifica daca primul operand este mai mic decat al doilea
print(f"Numarul 1 este mai mic decat numarul 2? {nr_1 < nr_2}")

# 2.4. OPERATORUL > este folosit pentru a verifica daca primul operand este mai mare decat al doilea
print(f"Numarul 1 este mai mare decat numarul 2? {nr_1 > nr_2}")

# 2.5. OPERATORUL != (not equal/nu egal) este folosit pentru a verifica daca cei doi operanzi au valori diferite
print(f"Numarul 1 este diferit de numarul 2? {nr_1 != nr_2}")

# 3. OPERATORI DE ATRIBUIRE: +=, -=, =, *=, /=

# ATENTIE!!! OPERATORII ++, -- din java NU EXIST in Python

# 3.1. Operatorul = -> Este folosit pentru a salva o information intr-o variabila
# atribuirea unei valori intiale intr-o variabila se numeste initializare

# atribuire prin initializare:
variabila_atribuire_initiala = 5  # am salvat valoarea 5 la adresa de memorie numita variabila_atribuire_initiala

# Atentie!!! Se poate face suprascriere. Adica daca la aceeași adresa de memorie facem o nouă atribuire,
# nu se va crea o noua variabila / adresa de memorie
# ci se va inlocui valoarea la adresa de memorie curenta

variabila_atribuire_initiala = 7  # atribuire prin suprascriere

# 3.1. Operatorul += va mari valoarea variabilei din stanga operatorului cu valoarea din dreapta operatorului
# rezultatul va suprascrie valoarea curenta din variabila
variabila_atribuire_initiala += 12  # rezultatul operatiei va fi 19

# 3.1. Operatorul -= va micsora valoarea variabilei din stanga operatorului cu valoarea din dreapta operatorului
variabila_atribuire_initiala -= 12  # rezultatul va suprascrie valoarea curenta din variabila

# 3.1. Operatorul *= va inmulti valoarea variabilei din stanga operatorului cu valoarea din dreapta operatorului
variabila_atribuire_initiala *= 5  # rezultatul va suprascrie valoarea curenta din variabila

# 3.1. Operatorul /= va imparti valoarea variabilei din stanga operatorului la valoarea din dreapta operatorului
variabila_atribuire_initiala /= 5  # rezultatul va suprascrie valoarea curenta din variabila

# 3. OPERATORI LOGICI: AND, OR, NOT

# ### OPERATORUL AND (strict) -> returneaza TRUE doar daca fiecare expresie returneaza TRUE

print(nr_1 < nr_2 and nr_1 <= nr_2)
# nr_1<nr_2 = TRUE, nr_1 <=nr_2 = TRUE, TRUE AND TRUE = TRUE

print(nr_1 < nr_2 and nr_1 >= nr_2)
# nr_1<nr_2 = TRUE,         nr_1 >=nr_2 = FALSE,        TRUE AND FALSE = FALSE

# ### OPERATORUL OR (mai putin strict) -> returneaza TRUE daca cel putin o expresie returneaza TRUE
print(nr_1 < nr_2 or nr_1 <= nr_2)
# nr_1<nr_2 = TRUE,		    nr_1 <=nr_2 = TRUE,		    TRUE OR TRUE = TRUE

print(nr_1 < nr_2 or nr_1 >= nr_2)
# nr_1<nr_2 = TRUE,		    nr_1 >=nr_2 = FALSE,	    TRUE OR FALSE = TRUE

print(nr_2 == nr_1 or nr_1 >= nr_2)
# nr_2==nr_1 = FALSE,	    nr_1 >=nr_2 = FALSE,	    FALSE OR FALSE = FALSE


# OPERATORUL NOT -> returneaza opusul expresiei

print(not nr_1 < nr_2)
# nr_1<nr_2 = TRUE,         NOT TRUE = FALSE

print(not nr_1 < nr_2 and nr_1 <= nr_2)
# nr_1<nr_2 = TRUE,         NOT TRUE = FALSE,       nr_1<=nr_2 = TRUE,      FALSE AND TRUE = FALSE

print(not nr_1 < nr_2 and nr_1 <= nr_2 or nr_2 > nr_1)
# nr_1 < nr_2 = TRUE,       NOT TRUE = FALSE,
# nr_1 <= nr_2 = TRUE,      FALSE AND TRUE = FALSE,
# nr_2 > nr_1= TRUE,        FALSE OR TRUE = TRUE

print(not nr_1 < nr_2 or nr_1 <= nr_2 and nr_2 > nr_1)
# nr_1<nr_2 = TRUE,         NOT TRUE = FALSE,
# nr_1<=nr_2 = TRUE,        nr_2 > nr_1= TRUE,
# TRUE AND TRUE = TRUE,     FALSE OR TRUE = TRUE

print((not nr_1 < nr_2 or nr_1 <= nr_2) and nr_2 > nr_1)
# nr_1<nr_2 = TRUE,         NOT TRUE = FALSE,
# nr_1<=nr_2 = TRUE,        FALSE OR TRUE = TRUE,
# nr_2 > nr_1= TRUE,        TRUE AND TRUE = TRUE

print(not ((nr_1 < nr_2 or nr_1 <= nr_2) and nr_2 > nr_1))
# nr_1<nr_2 = TRUE,     nr_1<=nr_2 = TRUE,      TRUE OR TRUE = TRUE,
# nr_2 > nr_1= TRUE,    TRUE AND TRUE = TRUE,   NOT TRUE = FALSE

# Ordinea prioritatii operatorilor logici:
# NOT > AND > OR (cu respectarea parantezelor, ca in aritmetica)
