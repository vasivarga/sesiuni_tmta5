"""
Listele in Python

Listele reprezinta adrese de memorie neomogene (pot stoca valori avand diverse tipuri de date)
care sunt ordonate pe baza de index si mutabile
mutabilitate = proprietatea unei structuri de date de a putea sa isi schimbe elementele
(exemplu: vreau sa mut elevul popescu in banca langa elevul ionescu)
Actiuni care se pot face asupra unei liste:
- adaugare elemente
- stergere elemente
- modificare element la un anumit index
- mutare element la un anumit index
Definirea listei se face pe baza unei perechi de paranteze patrate []
Se poate initializa si o lista goala
"""

# 1. Declararea si initializarea unei liste goale

# varianta 1
lista_studenti = []
print(f"Lista goala (v1) este: {lista_studenti}")
print(f"Dimensiunea listei goale este: {len(lista_studenti)}")

# varianta 2
lista_studenti = list()
print(f"Lista goala (v2) este: {lista_studenti}")
print(f"Dimensiunea listei goale este: {len(lista_studenti)}")


# Observatie: pot sa initializez o lista plecand de la un string prin apelarea functiei split()
string_test = "Astazi invatam despre liste"
lista_split = string_test.split()
print(lista_split)


# 2. Declararea si intializarea unei liste (omogene) populate
lista_studenti_prezenti = ["Adelina", "Anda", "Dida", "Dodo", "Elena", "Geanina", "Ioana", "Marcel", "Rodica", "Sabina"]
lista_studenti_absenti = ["Andrei", "Carmen", "Silvia", "Adina"]

# 3.a. Accesarea primului element din lista
# putem sa ne referim la un element cu un anumit index folosind paranteze drepte nume_lista[nr_index]
print(f"Elementul cu indexul 0 din lista cu prezentii este: {lista_studenti_prezenti[0]}")
print(f"Elementul cu indexul 0 din lista cu absentii este: {lista_studenti_absenti[0]}")

# 3.b Accesarea ultimului element din lista
print(f"Ultimul element din lista cu prezentii este: {lista_studenti_prezenti[-1]}")
print(f"Ultimul element din lista cu absentii este: {lista_studenti_absenti[-1]}")

# 4. Functii care pot sa fie folosite cu listele
# Functiile se pot apela prin intermediul numele listei urmat de punct

# 4.a Functia append() -> Adauga un element in lista la finalul listei
lista_studenti_prezenti.append("Vasi")
print(f"Lista de studenti dupa append este: {lista_studenti_prezenti}")

# 4.b Functia insert() -> Adauga un element in lista intr-o anumita pozitie
lista_studenti_prezenti.insert(3, "Cosmin")
print(f"Lista de studenti dupa insert este: {lista_studenti_prezenti}")

# 4.c Functia index() -> Returneaza indexul unui anumit element
print(f"Studentul 'Marcel' se afla in lista la indexul {lista_studenti_prezenti.index('Marcel')}")

# 4.d Functia remove() -> Sterge un element pe baza numelui sau
lista_studenti_prezenti.remove("Cosmin")
print(f"Lista de studenti dupa stergerea elementului 'Cosmin' este: {lista_studenti_prezenti}")

# 4.e Functia pop() -> Sterge ultimului element
lista_studenti_prezenti.pop()
print(f"Lista studenti dupa scoaterea ultimului element este: {lista_studenti_prezenti}")

# sau pe baza de index
lista_studenti_prezenti.pop(-2)
print(f"Lista de studenti dupa scoaterea penultimului element: {lista_studenti_prezenti}")

#Adaugam elementul 'Rodica' de doua ori apoi afisam lista din nou
lista_studenti_prezenti.append("Rodica")
lista_studenti_prezenti.append("Rodica")
print(lista_studenti_prezenti)

# 4.f Functia count() numara de cate ori apare un element intr-o lista
print(lista_studenti_prezenti.count("Rodica"))

# 4.g. Functia reverse() -> inverseaza elementele listei
lista_studenti_prezenti.reverse()
print(f"Lista de studenti inversata este: {lista_studenti_prezenti}")
#
# 4.h Functia extend() uneste listele prin comasare
lista_studenti_prezenti.extend(lista_studenti_absenti)
print(f"Lista dupa extend() >>>>  {lista_studenti_prezenti}")

# 4.i Functia append() adauga un element in lista la finalul listei
lista_studenti_prezenti.append("Cosmin")
print(f"Lista dupa append()  >>>> {lista_studenti_prezenti}")

# urmatoarea varianta creaza o lista imbricata
# lista imbricata (embedded list) = lista in lista
lista_studenti_prezenti.append(lista_studenti_absenti)
print(f"Lista dupa append() cu alta lista >>>> {lista_studenti_prezenti}")

#eliminam lista de studenti absenti
lista_studenti_prezenti.pop(len(lista_studenti_prezenti) - 1)

# 4.j Functia clear() -> sterge continutul listei
lista_studenti_prezenti.clear()
print(f"Lista studenti dupa apelarea metodei clear este: {lista_studenti_prezenti}")

# Adaugam inapoi toti studentii stersi => Extindem lista cu toate numele
lista_studenti_prezenti.extend(["Adelina", "Anda", "Dida", "Dodo", "Elena", "Geanina", "Ioana", "Marcel", "Rodica", "Sabina"])

# 4.k Functia sort() -> sorteaza lista in ordine alfabetica
lista_studenti_prezenti.sort()

print(f"Lista studenti dupa sortare este: {lista_studenti_prezenti}")
lista_studenti_prezenti.append("Cosmin")
lista_studenti_prezenti.sort()
print(f"Lista studenti dupa adaugarea lui Cosmin este: {lista_studenti_prezenti}")
# sortarea se va face in ordine alfabetica in functie de codul ASCII:
# https://infoas.ro/lectie/90/codul-ascii-tabel-complet

# 5. Crearea unei liste neomogene:
lista_neomogena = ["Adina", 23, True, "Cosmin", 30, False, "Elena", 25, True]

# 5.a Accesarea elementelor prin slicing (exact ca la stringuri)
# lista[index_start : index_stop : pas]
print(f"Persoanele din lista neomogena sunt: {lista_neomogena[::3]}")
print(f"Varsta lor este: {lista_neomogena[1::3]}")




