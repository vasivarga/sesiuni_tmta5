"""
Structura alternativa IF - este o modalitate prin care putem sa acoperim situatiile in care vrem sa
executam un set de instructiuni sau un altul in functie de rezultatul evaluarii unei conditii

Structura unei decizii (IF):
- Inceputul deciziei (If)
- Ramura din dreapta (TRUE) a deciziei -> reprezentata de primul bloc de cod dupa if
- Marcarea instructiunii alternative, cu conditie aditionala, atunci cand avem mai mult de doua situatii posibile (elif)
- Marcarea isntructiunii alternative finale - ultimul set de instructiuni,
in cazul in care niciuna dintre conditii nu este indeplinita.
Blocul de cod aferent fiecarei ramuri decizionale este marcat de indentare
Ramura decizionala = blocul de cod care se executa in cazul in care conditia este evaluata ca fiind adevarata si respectiv falsa
Indentare = spatiul lasat intre marginea fisierului si linia de cod

FORMA SIMPLA, GENERALA:

                        if expresie_1:
                            instructiune_1
                        elif expresie_2:
                            instructiune_2
                        else:
                            instructiune_3
"""

nr_1 = 5
nr_2 = 7

# IF SIMPLU (Fara alternative)
if nr_1 < nr_2:
    print(f"Am intrat pe ramura IF: {nr_1} este mai mic decat {nr_2}")

# IF CU CONDITIE ADITIONALA ELSE-IF
if nr_1 > nr_2:
    print(f"Am intrat pe ramura IF: {nr_1} este mai mare decat {nr_2}")
elif nr_2 == nr_1:
    print(f"Am intrat pe prima ramura ELSE-IF: {nr_2} este egal cu {nr_1}")
elif nr_2 > nr_1:
    print(f"Am intrat pe a doua ramura ELSE-IF: {nr_2} este strict mai mare decat {nr_1}")

# IF - ELSE (Conditie initiala + alternativa finala)
if nr_1 < nr_2:
    print(f"Am intrat pe ramura IF: {nr_1} este strict mai mic decat {nr_2}")
else:
    print(f"Am intrat pe ramura ELSE: {nr_2} este mai mare (sau egal) decat {nr_1}")

# IF - ELSE-IF - ELSE (Conditie initiala + conditie alternativa  + alternativa finala)
nr_3 = 5
nr_4 = 5

if nr_3 < nr_4:
    print(f"Am intrat pe ramura IF: {nr_3} este mai mic decat {nr_4}")
elif nr_3 > nr_4:
    print(f"Am intrat pe ramura ELSE-I: {nr_3} este mai mare decat {nr_4}")
else:
    print(f"Am intrat pe ramura ELSEȘ: {nr_3} este egal cu {nr_4}")

# CONCEPTUL NESTED IF (ÎMBRICAT, ADICĂ IF ÎN IF)

# IF CU CONDITIE ADITIONALA ELSE-IF
if nr_1 < nr_2:
    print(f"Am intrat pe ramura IF: {nr_1} este mai mic decat {nr_2}")
    if nr_1 % 2 == 0:
        print(f"{nr_1} este numar par")
    else:
        print(f"{nr_1} este numar impar")
elif nr_2 < nr_1:
    print(f"Am intrat pe ramura ELSE-IF {nr_2} este strict mai mic decat {nr_1}")

"""
Exercitiu:
Intre lunile noiembrie (inclusiv) si februarie (inclusiv), factura la curent se va calcula dupa urmatoarea formula:
- 0.68 lei pe kWh daca s-au consumat sub 100kWh pe luna
- 0.8 lei pe kWh daca s-au consumat intre 100kWh si 255kWh pe luna
- 1 leu pe kWh daca s-au consumat peste 250kWh
- in restul anului, pretul este unic, de 0.7 lei pe kWh

Daca persoana care plateste factura are peste 65 (inclusiv) de ani, i se aplica o reducere de 10%.

Se va scrie un program care face urmatoarele:
- citeste luna curenta reprezentata printr-un nr de la 1 la 12
- citeste varsta persoanei care plateste factura
- citeste numarul de kWh consumati pe luna respectiva
- afiseaza pretul total a facturii si daca s-a aplicat reducerea
"""

luna = int(input("Introduceti numarul lunii pentru care se plateste factura: "))
varsta = int(input("Introduceti varsta: "))
consum = float(input("Introduceti nr-ul de kWh: "))

valoare_factura = 0  # declaram variabila si o initializam cu 0
if luna >= 11 or luna <= 2:
    if consum < 100:
        valoare_factura = consum * 0.68
    elif 100 <= consum < 255:
        valoare_factura = consum * 0.8
    else:
        valoare_factura = consum * 1
else:
    valoare_factura = consum * 0.7

if varsta >= 65:
    valoare_factura -= valoare_factura * 0.1  # valoare_factura = valoare_factura - (valoare_factura * 0.1)
    print("Ati beneficiat de o reducere de 10%")

print(f"Factura este de {valoare_factura} RON")
