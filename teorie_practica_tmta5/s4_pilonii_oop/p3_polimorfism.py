"""
Polimorfism = principiu OOP care permite implementarea mai multor functii cu acelasi nume dar comportament diferit
exista mai multe modalitati de implementare a polimorfismului:
a) polimorfism prin definirea unei functii sau metode cu parametri impliciti
b) polimorfism prin definire unei functii sau metode cu *args
c) polimorfism prin reimplementarea metodei din clasa parinte

"""


# 1. Polimorfism prin functii cu parametri default (Method Overloading)
def sir_numere_pare(range_end, range_beginning=0, range_step=1):
    for i in range(range_beginning, range_end + 1, range_step):
        if i % 2 == 0:
            print(f"Numarul {i} este par")
        else:
            print(f"Numarul {i} este impar")


# Apelam aceeasi functie cu sau fara unele argumente default
sir_numere_pare(10)
sir_numere_pare(10, range_step=3)
sir_numere_pare(20, range_beginning=10, range_step=3)
print("-----------------------------------")



# 2. Polimorfism prin functii cu *args (Method Overloading)
def calcul_suma_numere(*numbers):
    suma = 0
    for number in numbers:
        suma = suma + number
    return suma


#Apelam aceeasi functie cu numar de argumente diferite
print(calcul_suma_numere(1))
print(calcul_suma_numere(2, 6))
print(calcul_suma_numere(578901256, 789013476, 56))
print("-----------------------------------")


def accesare_elemente_dictionar(**kwargs):
    for key, value in kwargs.items():
        print(f"Sucul {key} este de {value}L")


accesare_elemente_dictionar(pepsi=2, cola=3, fanta=5)
print("-----------------------------------")

accesare_elemente_dictionar(pepsi=2)
print("-----------------------------------")

sucuri = {
    "sprite": 3,
    "7Up": 2
}

accesare_elemente_dictionar(**sucuri)
print("-----------------------------------")


# Polimorfism prin reimplementarea metodei din clasa parinte in clasa copil
# Se mai numeste si Method Overriding
class Animal:
    def sound(self):
        print("sunet default")


class Catel(Animal):
    def sound(self):
        print("woof woof")


class Pisica(Animal):
    def sound(self):
        print("miau miau")


# instantiem un obiect de tip Animal
animal = Animal()

# Apelam metoda sound()
animal.sound()

# instantiem 1 obiect cu clasa Catel
goofy = Catel()

# observam ca metoda sound() si-a schimbat comportamentul in clasa Catel
goofy.sound()

# instantiem 1 obiect cu clasa Pisica
garfield = Pisica()

# observam ca metoda sound() si-a schimbat comportamentul in clasa Pisica
garfield.sound()

