from abc import ABC, abstractmethod

"""
Abstractizare = modalitate prin care obligam clasele care mostenesc sa defineasca un anumit comportament

Exista doua metode de abstractizare:

a) doar o parte din metodele dintr-o clasa sunt abstracte - clasa se va numi clasa abstracta
Daca definim o clasa copil care mostenste o clasa abstracta / interfata
si nu implementam metodele abstracte, atunci vom primi o eroare

b) toate metodele dintr-o clasa sunt abstracte - in acest caz clasa se va numi <<interfata>>

Putem spune ca o clasa abstracta functioneaza ca sablon pentru subclase. 
Clasele abstracte nu pot fi instantiate si necesită crearea unor subclase 
pentru a furniza implementari pentru metode abstracte. 

Modulul abc - Abstract Base Classes ne ajuta la crearea claselor abstracte

Orice clasa pe care o dorim sa fie abstracta trebuie sa mosteneasca 
proprietatile clasei ABC (Abstract Base Class/Clasa de Baza Abstracta)
"""


# Definim clasa abstracta Animal, care va fi o interfata
# Clasa Animal devine abstracta prin extinderea lui ABC (Clasa de baza abstracta)
class Animal(ABC):

    # Definim o proprietate abstracta <<sange>>
    # Atentie! Aceasta va fi o proprietate (atribut/field)
    # Desi seamana cu definirea unei metode, in clasele care vor extinde clasa Animal, <<sange>> va fi o proprietate
    # Pentru a defini proprietati abstracte, folosim decoratorul @property urmat de @abstractmethod (in ordinea asta)
    # Astfel obligam clasele care extind clasa Animal sa contina un atribut (field/proprietate) cu numele sange
    @property  # decorator care anunta ca este vorba de o proprietate (adica atribut/field)
    @abstractmethod  # anunta ca metoda (in cazul de fata proprietatea) abstracta, deci trebuie implementata in subclasa
    def sange(self):
        pass  # pass se poate folosi in acest caz, pentru a marca faptul ca aici nu este necesara o implementare

    # Definim inca o proprietate abstracta: <<nume>>
    @property
    @abstractmethod
    def nume(self):
        pass

    @abstractmethod
    def scoate_sunet(self):
        pass

    # In Python putem avea si implementari default in clase abstracte.
    def print_proprietati(self):
        print(f'Animalul {self.nume} are sangele {self.sange}')


# Declaram clasa <<Pisica>>
# Aceasta mosteneste proprietatile de la clasa Mamifer si este obligata sa implementeze tot din clasa Animal
class Pisica(Animal):
    nume = "pisica"
    sange = "cald"

    def scoate_sunet(self):
        print("Pisica face miau")


class Sarpe(Animal):
    nume = "sarpe"
    sange = "rece"

    def scoate_sunet(self):
        print("Sarpele face sssSSSss")