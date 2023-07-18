"""
Tupluri (tuples) in Python

Tuplurile reprezinta structuri de date ordonate si identificabile
pe baza de index care accepta duplicate si este imutabil (immutable)
"""
# 1. Definirea unui tuplu gol:
# varianta 1
tuplu_gol = ()
print(tuplu_gol)

# varianta 2
tuplu_gol = tuple()
print(tuplu_gol)

# 2. Definirea unui tuplu populat:
tuplu_populat = ("mere", "pere", "nuci", "covrigi")

# sau fara paranteze
greutate = 15, 6, 8, 1  # Daca definim o variabila in felul asta, va fi identifica automat ca si tuplu

print(greutate)

# 3. Functii care se pot folosi cu un tuplu
# 3.a Functia index returneaza indexul primului element dat ca parametru
print(f"Indexul fructului mere este: {tuplu_populat.index('mere')}")

# 3.b Functia count returneaza de cate ori apare un anumit element in tuplu
print(f"Fructul mar apare de {tuplu_populat.count('mere')} ori")
