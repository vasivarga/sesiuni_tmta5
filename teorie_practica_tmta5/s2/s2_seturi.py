"""
Seturi in Python

Seturile reprezinta structuri de date neordonate, imutabile
Operatii care se pot face intr-un set:
- accesare elemente
- adăugare elemente
- ștergere elemente
Definirea unui set se face cu o pereche de acolade
"""

# 1. Definirea unui set gol
set_gol = set()
print(type(set_gol))

# 2. Definirea unui set populat
set_pisici = {"tom", "garfield", "felix"}
set_catei = {"spike", "goofy", "pluto", "bethowen"}

# 3. Accesarea unui element din set
# Avand in vedere ca setul nu este indexat, NU putem accesa direct elementele din set
# Putem sa facem in schimb doua operatii similare:
# - parcurgerea setului cu for (vom face la cursul urmator)
# - putem sa verificam daca un element se afla in set cu operatorul IN
print("tom" in set_pisici)
assert "tom" in set_pisici, "Error: Tom nu exista in set_pisici"

# 4. Functii care pot fi folosite cu seturile
# 4.a functia add care adauga un nou element in set
set_pisici.add("Jinx")
set_pisici.add("Jinx")
set_pisici.add("Jinx")

# Observam ca set-ul nu permite duplicate. Chiar daca am adaugat Jinx de 3 ori, el apare doar o singura data
print(f"Set pisici dupa adaugarea lui Jinx: {set_pisici}")

# 4.b Functia pop() sterge un element la intamplare dar ne si returneaza inpoi elementul sters
# pe care putem sa-l punem intr-o variabila daca mai avem nevoie de el
item_sters = set_pisici.pop()
print(f"Setul dupa stergerea elementului cu pop() este: {set_pisici}")
print(f"Elementul sters cu pop() este: {item_sters}")

# 4.c Functia remove() sterge un element specificat
set_pisici.add("meow")
set_pisici.remove("meow")
print(f"Setul dupa stergerea elementului 'meow' cu remove() este: {set_pisici}")

set_pisici.discard("meow")
# print("am trecut pe aici")

# Diferenta intre remove() si discard() este ca remove da eroare daca elementul nu exista
# si discard executa instructiunea dar nu da eroare daca elementul nu exista

# 4.c Functia update si functia union concateneaza doua seturi
set_pisici.update(set_catei)
print(f"Set pisici dupa update(): {set_pisici}")
set_rezultat = set_pisici.union(set_catei)
print(f"Set pisici dupa union(): {set_rezultat}")

# Diferenta intre update() si union() este ca update modifica lista de la care se pleaca direct,
# in schimb union creaza o a treia lista
# care reprezinta concatenarea celor doua liste implicate

# 4.c Functia clear() sterge continutul setului
set_pisici.clear()
print(f"Set pisici dupa clear(): {set_pisici}")