#Ex_1 - În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

'''o adresa de meorie unde se salveaza valori. Valorile se pot modifica pe parcursul rularii codului (suprascriere)'''

#Ex_2 - Declară și inițializează câte o variabilă din fiecare din următoarele tipuri:int, string, float, boolean
elev = "Tutuca Petre" #string
varsta = 35 #integer
media_la_bac = 7.52  #float
promovat = True  #boolean

#Ex_3 - Utilizează funcția type pentru a verifica dacă variabilele declarate mai sus au tipul de date așteptat.

print(type(elev))
print(type(varsta))
print(type(media_la_bac))
print(type(promovat))
print(f'Variabilele noastre sunt de urmatoarele tipuri: {type(elev)}, {type(varsta)}, {type(media_la_bac)}, {type(promovat)}')
print(f'Variabilele noastre sunt de urmatoarele tipuri: {type(elev), type(varsta), type(media_la_bac), type(promovat)}')
print(type(elev), (varsta))


#Ex_4 - Rotunjește variabila ‘float’ folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere),
# apoi verifică din nou tipul de date al acesteia.


print(round(media_la_bac,1))   #varianta scurta, rotunjire la o singura decimala

media_la_bac = round(media_la_bac)  #rotunjire la numar intreg
print(media_la_bac)


#Ex_5 - Incearca sa convertesti variabila string la int folosind type casting si observa rezultatele

''' Type Casting poate fi folosit in convertirea din string in integer, dar si din integer in string'''
#exemplul 1
# var1 = "2"
# print(type(var1))
# var1 = int(var1)
# print(type(var1))
# #exemplul 2
# var2 = 3
# print(type(var2))
# var2 = str(var2)
# print(type(var2))
# print(int(elev))

#Ex_6 - Incearca sa convertesti variabila boolean la int folosind type casting si observa rezultatele

promovat = False
print(int(promovat))

#Ex_7 - Schimba valoarea variabilei boolean (din true in false sau din false in true) si repeta exercitiul anterior

promovat = True
print(int(promovat))


elev = "Tutuca Petre" #string
varsta = 35 #integer
media_la_bac = 7.52  #float
promovat = True  #boolean

#Ex_1 -  Folosește funcția print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip pe rand prin toate modalitatile cunoscute

#print("numele elevului este " + nume + " re varsta de " + varsta + " a luat nota " + media_la_bac + "a promovat " + promovat)
#print("numele elevului este " + nume + " re varsta de " + str(varsta) + " a luat nota " + media_la_bac + "a promovat " + promovat)
#print("numele elevului este " + nume + " re varsta de " + str(varsta) + " a luat nota " + str(media_la_bac) + "a promovat " + promovat)
print("Numele elevului este " + elev + ", are varsta de " + str(varsta) + " ani, a luat nota " + str(media_la_bac) + " si a promovat " + str(promovat))
print(f'Numele elevului este {elev}, are varsta de {varsta} ani, a luat nota {media_la_bac} si a promovat {promovat}')

#Ex_2 - Citește de la tastatură numele și prenumele unei persoane și salveaza-le in cate o variabila.
# Afișează pe ecran următoarea propoziție: 'Numele complet are x caractere'.

nume = "Tutuca"
prenume = "Petre"
'''
cal = 1   "000 110 001"
          " c   a   l "
Cal = 1   "010 110 001"
          " C   a   l
declarare si initializare de variabile diferite
adrese de memorie diferite, nu este suprascriere
'''
lungime_nume = len(nume)  #functie len() aduce un rezultat de tip integer
print(lungime_nume)
lungime_prenume = len(prenume)
print(lungime_prenume+lungime_nume)
#varianta scurta
print(len(nume) + len(prenume))
print(len(nume + prenume))
print(len(nume + " " + prenume))
#print(len(nume)+ " " + len(prenume))        o lasam comentata pentru a putea rula cod in continuare
print(len(nume) + len(" ") + len(prenume))




#Ex_3 - Citește de la tastatură lungimea și lățimea unui dreptunghi și salveaza-le in cate o variabila.
# Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.
lungime = 9
latime = 3
print(f"Aria dreptungiului este: {lungime*latime}")
aria = lungime*latime
print(f"Aria dreptungiului este: {aria}")


#Ex_4 - Având stringul: 'Coral is either the stupidest animal or the smartest rock' afișează de câte ori apare
# cuvântul 'the' în acest string
propozitie = 'Coral is either the stupidest animal or the smartest rock'
x = "the"
print(propozitie.count(x))
print(propozitie.count("the"))


#EX_5 Folosindu-te de string-ul de la exercițiul 4, inlocuieste “the” cu “THE” peste tot (inclusiv in cuvantul “either”)
# si afișează pe ecran rezultatul

print(propozitie.replace(x, x.upper()))

#Ex_6 Folosindu-te de string-ul de la exercițiul 4 foloseste un assert ca să verifici dacă acest string conține doar numere.
assert propozitie.isnumeric() == False, "Stringul nu contine doar numere"

''' operatiunea  expected_result == actual result, "error message" '''

# assert propozitie.isnumeric() == True, "Stringul nu contine doar numere"

# triunghi = "isoscel"
# scos_de_pe_pagina = "echilateral"
#
# # 5 verificati cu un assert daca triungiul este de tip echilateral
# expected_result = "echilateral"
# actual_result = triunghi  #extragem raspunsul din variabila declarata anterior
# #actual_result = scos_de_pe_pagina
#
# '''
# =  declarare
# == comparatie
# '''
# # assert expected_result == actual_result, "Triungiul nu este echilateral"
# # assert "echilateral" == triunghi, "Triungiul nu este echilateral"
# # assert "echilaterl" == "isoscel", "Triungiul nu este echilateral"
#
#
# expected_result = "echilateral"
# actual_result = "isoscel"
# #assert expected_result == actual_result, "Triughiul nu este echilateral"
# assert expected_result != actual_result, "Triunghiul este echilateral"
#
#
# ''' operatiunea  expected_result == actual result, "error message" '''
#
# expected_result = "echilateral"
# actual_result1 = "isoscel"
# actual_result2 = "echilateral"
# assert expected_result == actual_result1, "Triunghiul nu este echilateral"
# assert expected_result != actual_result2, "Triunghiul nu este echilateral"


# Ex_1 Citește de la tastatură un string de dimensiune impară și afișează caracterul din mijloc.
'''
cuvantul = "cascaval"
print(cuvantul[0])
print(cuvantul[1:3])   # la pozitia de inceput a slicingului va fi cea declara (in cazul nostru 1)
                       # pozitia de fianl a slicingului va fi poitia declarata minus un caracter
print(cuvantul[1:4])
print(cuvantul[0:7:1])     # ultima segventa ne da pasul
print(cuvantul[0:7:2])
print(cuvantul[0:7:3])
'''
cuvantul = str(input("Introduceti cuvantul: "))
print(cuvantul)
print(cuvantul[int(len(cuvantul)/2)])

'''
cuvant = maxim
len(cuvant) = 5
len(cuvant)/2   ->  5/2 = 2.5
int(len(cuvant)/2)  -> scoate partea intrega 5/2 -> 2
slicing - zicem din cuvant scoate caracterul cu pozitia (int(len(cuvant)/2) adica litera de pe pozitia 2
in cazul nostru "x"
'''


# Ex_2 Folosind assert, verifică dacă un string este palindrom.
# palindrom = o serie de caractere care citite invers sunt acelasi lucru (in oglina)
# pali = "12321"
# assert pali == pali[::-1], "Nu este palindrom"

# pali2 = "12345"
# assert pali2 != pali2[::-1], "Este palindrom"
# assert "12345" != "54321", "Este palindrom"
# assert "12345" == "54321", "Nu este palindrom"


# Ex_3 - Citește un string de la tastatură (ex: 'alabala portocala') asupra caruia sa efectuezi urmatoarele:

# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.
prop = "mare soare" #input("Introduceti cuvantul: ")

variabila1, variabila2 = "cas", 3
print(variabila1)
print(variabila2)

cuv1, cuv2 = prop.split(" ")
print(cuv1)
print(cuv2)
'''
prop = "alabala portocala"
cuv1, cuv2 = prima parte din prop pana la spatiu , a doua parte din prop dupa spatiu
cuv1, cuv2 = alabala, portocala
'''
prop = "mare soare"
cuv1, cuv2, cuv3 = prop.split("r")
print(cuv1)
print(cuv2)
print(cuv3)

# Ex_4 - Citește un string de la tastatură (ex: alabala portocala) asupra caruia sa efectuezi urmatoarele:

# salvează primul caracter într-o variabilă
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.

cuvant = "alabala portocala" #input("introduceti cuvantul")
litera = cuvant[0]
#litera = "a"
capitalizare = litera.upper()
#capitalizare = "A"
partial = cuvant[1:-1]
#partial = "labala portocal"
noul_cuvant = litera + partial.replace(litera,capitalizare) + litera
#noul_cuvant = a + lAbAlA portpcAl + a -> alAbAlA portocAla
print(noul_cuvant)


# Ex_5 - citeste un user de la tastatura, citeste o parola. Afiseaza: 'Parola pt user x este ***** si are x caractere
user = "maxim"
parola = "maxsadfgherstdyguih"
print(f'Parola pentru user {user} este {"*"*len(parola)} si are {len(parola)} caractere')
print(f'Parola pentru user {user} este ***** si are {len(parola)} caractere')


#Ex_1 Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else

'''
Structura if else, putem sa o consideram ca pe o intersectie.
Daca conditia este adevarata mergem la dreapta si executam codul
Daca conditaeste falsa mergem la stanga si executam codul/ skip
'''

#Ex_2 Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)
x = 7

if x >= 0 and type(x) == int:
    print(f'{x} este numar natural')
else:
    print(f'Numarul {x} nu este numar natural')

#Ex_3 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

if int(x) > 0:
    print("numar pozitiv")
elif int(x) < 0:
    print("numar negativ")
else:
    print("neutru")


#Ex_4 Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

# if x >= -2 and x <= 13:
#     print("numarul este inclus in intervalul -2 13")
# else:
#     print("nu este inclus in interval -2 13")



#Ex_5 Verifica daca x NU este intre 5 si 27, excluzand capetele de interval. (a se folosi ‘not’)
x = 7

if not(x >5 and x < 27):   #if not(x>5)  and not(x<27)
    print("numarul nu este in interval")
else:
    print("numarul este in interval")

# if not x > 5 and not x < 27:       # expresia contine o dubla negatie - Not >5 si not < 27 || si Not < 27
#     print("nu este in interval")
# else:
#     print("este in interval")


#Ex_6 Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale, daca nu, afiseaza care din ele este mai mare
x = 8
y = 8
if x > y:
    print(f'{x} este mai mare ca {y}')
elif y > x :
    print(f'{y} este mai mare ca {x}')
else:
    print("numerele sunt egale")

#Ex_7 Presupunand ca x, y, z (toate de tip int) reprezinta laturile unui triunghi, afiseaza daca triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).
x = 3
y = 6
z = 9
if x == y and x == z and y == z:
    print("triunghi echilateral")
elif x == y or x == z or y == z:
    print("triunghi isoscel")
else:
    print("triunghi oarecare")

#Ex_8 Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
litera = "E"  #input(str("introduceti litera = "))
if litera.upper() == "A" or litera.upper() == "E" or litera.upper() == "I" or litera.upper() == "O" or litera.upper() == "U":
    print("litera este vocala")
elif litera.isdigit():
    print("caracterul introdus nu este litera")
else:
    print("litera este consoana")

lita_vocale = ["A", "E", "I", "O", "U"]
if litera.upper() in lita_vocale:
    print("litera este vocala")
else:
    print("litera este consoana")

'''
Calculare pret discount

Dacă un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.
În caz contrar, dacă clientul nu are peste 65 de ani, dacă persoana călătorește cu cel puțin un copil va avea o reducere de 10%
Atat pentru seniori cat si pentru non- seniori se va aplica o reducere suplimentara de 10% daca vor calatori in timpul iernii.
De asemenea, atât pentru seniori, cât și pentru non seniori se va aplica o taxă de lux de 3% dacă vor călători în clasa I (în orice sezon) sau 1% taxă de gestiune în caz contrar.
'''
varsta_client = 66
discount = 0
copii = False
sezon = "iarna"
clasa = "2"
pret = 100

if varsta_client > 65:
    discount = 0.15
elif copii == True:
    discount = 0.1
if sezon == "iarna":
    discount += 0.1  # discount = discount + 0.1
if clasa == "1":
    tax = 0.03
else:
    tax = 0.01
pret_calatorie = pret - (pret*discount) + (pret*tax)
print(f'Pretul excursiei este: {pret_calatorie}')


'''
Calculare discount seller

Compania X vinde mărfuri la punctele de vânzare cu ridicata și cu amănuntul. 
Clienții angro primesc o reducere de două procente la toate comenzile. 
De asemenea, compania încurajează atât clienții angro, cât și clienții cu amănuntul
să plătească ramburs la livrare, oferind o reducere de două procente pentru această 
metodă de plată. Încă o reducere de două procente este acordată pentru comenzile de 
50 sau mai multe unități. 

'''
client_angro = True  #False
reducere = 0
cantitate = 50
ramburs = True  #False
pret = 100
if client_angro:
    reducere = 0.02
if ramburs:
    reducere += 0.02
if cantitate >= 50:
    reducere += 0.02
pret_final = pret - (pret*reducere)
print(f'Pretul total al comenzii este {pret_final}')

'''
Introduceti un nume de film de la tastatura si evaluati daca numele acelui film este 
numele filmului vostru preferat. Daca da, atunci printati pe ecran: 
“Acesta este filmul meu preferat”. In caz contrar printati pe ecran: 
“Din pacate nu este filmul meu preferat”
'''
film = "Terminator"   #input("Introduceti filmul: ")
film_preferat = "Titanic"
if film == film_preferat:
    print("Acesta este filmul meu preferat")
else:
    print("Din pacate nu este filmul meu preferat")


"""
Aveti la dispozitie urmatorul database url:
jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC
host = jdbc:mysql://
baza_de_date = mysql.db.server
:3306 = portul de access
/my_database?useSSL=false&serverTimezone=UTC = 

SELECT "cereneala" FROM "nume tabel"
WHERE filter and filter
ORDER by ASC sau DESC

Extrageti din acest text numele bazei de date: mysql.db.server
Folositi un if statement pentru a evalua daca numele bazei de date 
este cel corect (presupunand ca extrageti url-ul dintr-un sistem extern si 
nu stiti care este acesta)
"""
data_base_link = "jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC"
expected_data_base_name = "mysql.db.server"
link_without_host = data_base_link[data_base_link.index("/")+2: len(data_base_link)]
data_base_name = link_without_host[0:link_without_host.index(":")]
if data_base_name == expected_data_base_name:
    print("baza de date este corecta")
else:
    print("baza de date nu este corecta")
