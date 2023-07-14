"""
################# 1. TERMENI GENERALI #################

Compilare
- executarea/rularea codului scris de catre programator, traducere din ‘human reading syntax’ in ‘machine language’

IDE - Integrated Development Environment (Mediu de Dezvoltare Integrat)
- Este locul in care putem sa scriem si sa rulam cod
- Vine in ajutorul programatorilor avand o serie de functionalitati care fac programarea mai usoara
- Are terminal, consola, venv (in cazul PyCharm)
- Ex: PyCharm (Python), IntelliJ (Java), Visual Studio (C/C++/C#), VSCode(mai multe limbaje), etc

Terminal
- o interfata prin care putem comunica cu sistemul de operare
- de aici putem accesa fisiere, putem rula programe, putem modifica setari
- integrat si cu limbajele de programare/frameworkuri (ex: putem rula programe python direct din terminal)

Consola
- interfata pentru output (rezultatul executarii codului) si input (cand se asteapta input de la user)
- in PyCharm consola se gaseste in partea de stanga-jos, tab-ul denumit "Run"

venv (Virtual Environment)
- Multe programe scrise in Python folosesc librarii externe (bucati de cod/package-uri scrise de altii)
- Aceste librarii pot avea mai multe versiuni (se fac imbunatatiri/adaugari de functionalitati noi)
- Unele versiuni ale librariilor externe pot fi compatibile sau nu cu anumite versiuni de Python
- venv este un mediu virtual care ne ajuta sa izolam aceste versiuni in functie de nevoile pe care le avem pt proiect,
- fiecare proiect Python va avea propriul venv in care se vor putea instala/adauga librarii externe
"""

a = 5
b = 3
c = a + b

print(c)

x = "Hello world"
print(x)

x = "Bye world"
print(x)


"""
################# 2. VARIABILE ################# 

- Sunt adrese de memorie la care noi putem sa stocam informatii
- Numele variabilei este de fapt numele adresei de memorie la care sunt stocate informatiile
- Numele variabilelor trebuie sa respecte anumite reguli:
a) trebuie sa inceapa cu litera mica (conventie)
b) nu are voie sa inceapa cu cifra sau caractere speciale (obligatoriu)
c) nu trebuie sa contina spatii (obligatoriu)
d) nu pot fi cuvinte rezervate de Python (obligatoriu), ex: print, False, input
e) numele trebuie sa urmeze formatul camelCase sau snake_case
f) numele variabilelor este case-senstive (adica variabila numepisica nu este egala cu variabila numePisica)
g) numele variabilelor este unic. Daca vom incerca sa facem o redefinire, 
de fapt sistemul nu va aloca o alta adresa de memorie ci va schimba informatia de la adresa de memorie deja alocata
"""

# Formatul textului din punct de vedere al Case Style-ului poate fi:

# a) camelCase - cel mai folosit la numirea variabilelor (mai ales in Java)
# b) snake_case - folosit la numirea variabilelor (mai ales in Python)
# c) PascalCase - folosit la numirea claselor (cam in toate limbajele)
# d) kebab-case - cel mai folosit in url-uri si la numirea endpoint-urilor

# Declarare si initializare variabila:
nume = "Andrei"

'''
In randul de mai sus
1. s-a declarat variabila nume (careia i s-a alocat o zona in memorie)
2. i s-a facut initializarea, adica i s-a atribuit valoarea "Alin"

"Andrei" trebuie scris intre ghilimele pentru a fi considerat text dat de la tastatura si nu numele unei alte variabile
Daca nu era intre ghilimele, sistemul ar fi cautat variabila numita "Andrei". Nu ar fi gasit-o si ar fi returnat eroare
'''

# daca nu folosesc variabila 'nume', ea va fi marcata cu galben ca si atentionare ca nu am folosit continutul anterior
nume = "Andreea"  # momentul in care dau o alta valoare pentru o variabila se numeste suprascriere

print(nume)

prenume, nume, varsta = "Cristi", "Pop", 25
# am facut o dubla declarare si initializare, care este posibil in Python
# am anuntat sistemul ca vrem sa declaram doua variabile, 'prenume' si 'varsta' prin folosirea virgulei
# in dreapta egalului am specificat valorile cu care vrem sa initializam cele doua variabile, in ordinea declararii lor


# Metode "legale" de denumire de variabile (la care compilatorul nu va da eroare):
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Metode ilegale de denumire de variabile (avem eroare la fiecare denumire):
# 2myvar = "John"
# my-var = "John"
# my var = "John"


"""
################# 3. CONSTANTE ################# 
Constantele sunt variabile ale căror valori nu se schimbă în timpul execuției programului. 

Convenții care ne ajuta la definirea și folosirea constantelor:

1. Denumirea cu majuscule
2. Definirea la începutul programului/fisierului
3. Păstrarea valorii variabilei pe tot parcursul programului
"""

PI = 3.14
INSCRIS_LA_CURS = True


"""
################# 4. TIPURI DE DATE ################# 
- Tipul datei precizeaza ce valori poate avea acea data (variabila) și ce operatii se pot face cu ea.

Exista patru tipuri de date primitive in Python:
# string -> au valori de tip text
# int -> au valori numerice intregi (pozitive sau negative)
# boolean -> pot avea doar doua valori: True sau False
# float -> pot stoca numere cu zecimale (adica numere cu virgula)

Tipul de data in python nu este specificat in mod explicit ca in Java/C, ci rezulta din valoarea stocata in variabila
Asta este motivul pentru care putem sa facem schimbare de tip de data

Tipurile de date pe care le facem astazi se numesc tipuri de date primitive/simple.
Mai exista si tipuri de date derivate, dar ele au la baza tot tipuri de date simple.
"""

variabila_string = "Hello world"  # am declarat si initializat o variabila cu tipul de date string
print(variabila_string)
print(type(variabila_string))

# INT (INTREG)
variabila_int = 34
print(variabila_int)
print(type(variabila_int))

# ATENTIE! Aici, daca o pun intre ghilimele este de tip string si nu int:
# variabila_int = "34"

# FLOAT
variabila_float = 3.14  # am declarat si initializat o variabila float. Obs: se foloseste punct (.) nu virgula (,)
print(variabila_float)
print(type(variabila_float))

# ATENTIE! Urmatoarea instructiune nu va stoca o valoare, ci va stoca un tuplu (Curs 3):
# variabila_float_redeclarata = 3,14
# print(variabila_float_redeclarata) # afiseaza un tuplu format din numerele 3 si 14

# BOOLEAN
variabila_boolean_true = True
variabila_boolean_false = False
print(variabila_boolean_true)
print(variabila_boolean_false)
print(type(variabila_boolean_true))
print(type(variabila_boolean_false))

# ATENTIE! Urmatoarea instructiune va da eroare pentru ca va cauta o variabila numita false:
# variabila_boolean_false = false

# ATENTIE! Aici este string si nu boolean:
# variabila_boolean_false = "False"

"""
################# 5. FUNCTIA type() SI TYPE CASTING ################# 
Type casting se referă la procesul de transformare a unei valori sau a unei expresii de un anumit tip de date 
în alt tip de date.
"""

a = "5"
b = 3

print(type(a))
print(type(b))


# Daca dorim sa facem suma intre a + b (adica 5+3), trebuie sa convertim string-ul din variabila a intr-un numar intreg,
# altfel avem eroare
# print(a + b) - ne da eroare

print(int(a) + b)

# Daca dorim sa lipim textul a de textul b (adica 53), trebuie sa convertim nr-ul intreg din variabila b intr-un numar
# string, altfel avem eroare
print(a + str(b))

# Dacă facem casting dintr-un float la int, se va returna partea întreagă a numărului icu tipul de data float
d = 3.6
print(int(d))

# Daca facem casting dintr-o variabila bool intr-o variabila int se va converti din True in 1 sau din False in 0
n = True
m = False

print(int(n))
print(int(m))

"""
################# 6. COMENTARII ################# 

- sunt linii de cod pe care le putem scrie sub forma de explicatii si care sunt ignorate de compilator

Exista doua tipuri de comentarii:
1. comentarii multi-line -> comentarii care se pot scrie pe mai multe linii. 
Sunt reprezentate de un text scris intre doua perechi de trei ghilimele sau apostroafe.
2. comentarii single-line -> comentarii care se pot scrie pe o singura linie. 
Sunt reprezentate de un text precedat de semnul #

Ca sa putem sa comentam mai multe linii in acelasi timp sau sa comentam automat o linie cu comentariu single line
ne putem folosi de scurtatura CTRL + "/" (pe Windows) sau COMMAND + "/" (pe Mac)
"""

# one line comment

""" Multi - line
comment """

'''Another multi - line
comment'''

print("Hello world")


"""
################# 7. FUNCTIA print() #################

Functia print este o metoda prin care putem sa afisam informatii in consola

Structura functiei print este urmatoarea:
1. numele functiei (print)
2. valoarea pe care vrem sa o afisam (text, numere, caractere speciale etc)
- Daca vrem sa printam text, este foarte important sa fie pus intre ghilimele sau apostroafe. 
- In caz contrar, sistemul va crede ca este o variabila, pe care nu o va gasi si va returna eroare

In limbajele de programare in general semnul ghilimele reprezinta delimitator de text
- Orice text este pus intre ghilimele de inceput si ghilimele de final
- Daca incercam sa scriem un al doilea text intre ghilimele in interiorul unui text intre ghilimele, 
atunci sistemul va considera ghilimelele de inceput al celui de-al doilea text ca fiind sfarsitul primului text     
"""

print("Hello world")
print('Hello world')  # putem sa specificam textul si intre ghilimele

# ATENTIE! Sistemul va considera in cazul urmator ca textul meu este "Hello", iar Anton este o variabila separata
# print("Hello "Anton" ")

# Optiuni pentru problema cu limita de text:
#  1. scriem ghilimele in apostroafe
print('Hello "Anton"')
# 2. scriem apostroafe intre ghilimele
print("Hello 'Anton'")
# 3. folosim escape character "\" care instruieste sistemul sa trateze urmatorul caracter nu ca pe un caracter special
# ci ca pe un text de afisat pe ecran
print("Hello \"Anton\"")
print('Hello \'Anton\'')

"""
PRINT: Concatenare
Concatenare = lipirea a doua texte (string-uri) separate intr-unul singur
"""
# Exemplu:
text1 = "Afara ploua "
text2 = "Imi place? "
text3 = "Nu, as vrea sa ninga. "
string_concatenat = text1 + text2 + text3

print(string_concatenat)

print(text1 + text2 + text3)

ora_curenta = 20
# ATENTIE! Urmatoarea instructiune va returna eroare: TypeError: can only concatenate str (not "int") to str
# print(string_concatenat + "Este ora" + ora_curenta)

# concatenarea se poate face doar intre string-uri
# concatenarea cu alt tip de data este incompatibila
# in cazul asta specific nu va functiona pentru ca semnul "+" are o semnificatie diferita
# pentru string (concatenare) vs int (adunare)

# Optiuni:
# 1. Pot sa definesc direct valoarea orei intre ghilimele
# (nu este neaparat o optiune pentru ca nu putem controla tot timpul tipul de data al variabilelor pe care le primim)
# 2. Type casting
print(" Este ora " + str(ora_curenta))
# 3. Printare cu formatare
print(f"Este ora {ora_curenta}")


"""
################# 9. Assert ################# 
Assert este un cuvant care este tradus ca evaluare
Din punct de vedere tehnic inseamna o comparatie intre doua valori
- Daca comparatia returneaza True, sistemul va merge mai departe cu executarea urmatoarei instructiuni
- Daca comparatia returneaza False, sistemul va opri executia programului curent si va returna eroare: AssertionError

Componentele unui assert:
1. keyword-ul assert care anunta sistemul ca urmeaza o evaluare
2. valorea pe care o comparam
3. operatorul de comparare
4. valoarea cu care comparam
5. mesajul de eroare pe care sa il returneze atunci cand comparatia returneaza False (optional)

Este foarte folosit in testele automate.
"""

# imi_place_programarea = False
# assert imi_place_programarea == True, "Eroare, nu imi place programarea"
# print("Am trecut de assert, imi place programarea :)")

# user = "abcUser"
# expected_password ="pass123"
# inserted_password = input("Va rugam sa inserati parola: ")
# print(expected_password==inserted_password) # printeaza rezultatul evaluarii
# assert expected_password==inserted_password,"Eroare: parola gresita, mai aveti doua incercari"

# Functia input returneaza valori de tip string.
# Ca sa putem sa le procesam ca int trebuie sa facem type casting

# In exemplul comentat de mai jos nu se va afisa nimic in consola inainte sa se citeasca datele de la tastatura
# a = input()
# b = input()

# In exemplul de mai jos se va afisa un text inaintea citirii datelor de la tastatura
a = int(input("Va rugam sa introduceti primul numar: "))
b = int(input("Va rugam sa introduceti al doilea numar: "))

suma = a + b
print(suma)

# sau varianta fara variabila:
# print(int(a) + int(b))

