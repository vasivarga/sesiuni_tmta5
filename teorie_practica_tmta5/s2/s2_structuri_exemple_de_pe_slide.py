date_plata_facturi = [1, 10, 15, 20, 25, 30]
data_plata_factura = 15

i = 255

for i in range(len(date_plata_facturi)):
    if date_plata_facturi[i] == data_plata_factura:
        print(f"Factura a fost platita in ziua de {date_plata_facturi[i]}, nu mai mananci la lumanare.")
        break
    print(f"Data de astazi este: {date_plata_facturi[i]}, in continuare mananci la lumanare.")

print("-----------------------------------------")

for data in date_plata_facturi:
    if data == data_plata_factura:
        print(f"Factura a fost platita in ziua de {data}, nu mai mananci la lumanare.")
        break
    print(f"Data de astazi este: {data}, in continuare mananci la lumanare.")

print("-----------------------------------------")

suma = 0
for i in range(0, 11):
    rest = i % 2
    if rest == 0:
        continue
    suma += i

print(f"Suma numerelor impare de la 0 la 10 este: {suma}")

print("-----------------------------------------")


for i in range(1, 16):
    rezultat_impartire = i / 2
    rest = i % 2
    print(f"Rezultatul impartirii lui {i} la 2 este {rezultat_impartire}, si avem rest de {rest}")

print("-----------------------------------------")


for i in range (0, 11):
    if i % 2 == 0:
        print(f"Numarul {i} este par")
    else:
        continue
    print(f"A fost executat continue pentru i = {i}")

print("-----------------------------------------")

