"""
POO = Programare orientata pe obiecte
OOP = Object Oriented Programming

CLASA = structura de tip (tipar/blueprint/prototip) care serveste drept ghid pentru un element care ar PUTEA exista
Practic, clasa este o reprezentare a unui obiect sau a unei entitati care poate exista.

Componentele unei clase:

1. ATRIBUTE (field-uri, proprietati) = proprietatile cu care se vor identifica obiectele

    - pentru a accesa un atribut dintr-o clasa in interiorul acelei clase se foloseste keyword-ul self
    in caz contrar se va considera ca se face referinta catre parametrii metodei

    - accesarea unui atribut dintr-o clasa in afara clasei se poate face in urmatoarele moduri:
        a) un obiect instantiat din acea clasa
        b) decoratorul @staticmethod pentru a accesa atributele si metodele clasei
        c) prin conceptul de mostenire a unei clase (vom discuta la cursul 7)

    - atributele pot avea valori implicite daca exista niste valori general valabile

    - daca nu exista valori general valabile atunci atributele vor avea valoarea initiala None

2. METODE = Actiunile pe care le poate face un obiect/o entitate
            ATENTIE! Metodele sunt de fapt functii create in interiorul clasei
            In afara clasei = functii
            In interiorul clasei = metode

3. CONSTRUCTOR = Element care va fi folosit pentru instantierea obiectelor dintr-o clasa
Scopul unui constructor este de a ajuta sistemul sa instantieze obiectul dintr-o clasa
Exista doua tipuri de constructori:

a) constructor explicit care obliga utilizatorul sa populeze anumite atribute la instantierea	obiectului
si daca este cazul sa defineasca o regula de populare a atributelor

b) constructor implicit care este apelat automat atunci cand nu exista un constructor explicit definit

In python nu e posibila definirea mai multor constructori

OBIECT = instanta a clasei, reprezentare reala a tiparului reprezentat de clasa pot sa instantiez oricate obiecte
dintr-o anumita clasa
"""


class Masina:
    marca: str = None
    model: str = None
    culoare: str = None
    an_fabricatie: int = None
    viteza_maxima: int = 250
    viteza_curenta: int = 0
    este_pornita: bool = False

    # definim constructorul explicit al clasei
    def __init__(self, marca, model, culoare):
        # pentru a ne referi la atributele clasei, se va folosi <<self>>

        # argumentele din __init__ <<marca, model, etc>> nu sunt identice cu field-urile din clasa, ele
        # sunt denumite la fel tocmai pentru a scoate in evidenta diferentele dintre acestea
        # valorile din __init__ vor veni atunci cand vom declara un obiect de tip Masina

        # aici intalnim conceptul de polimorfism, despre care vom discuta la cursul urmator

        # deci <<self.culoare>> se refera la variabila declarata la inceputul clasei,
        # iar <<culoare>> din __init__ va fi valoarea pe care o primeste obiectul de tip Masina() la initializare
        self.marca = marca
        self.culoare = culoare
        self.model = model

    """
    Actiuni:
    - pornire
    - accelerare
    - decelerare
    - oprire
    - claxon
    """

    # definim metoda porneste_masina()
    def porneste_masina(self):
        self.este_pornita = True
        print("Am pornit masina")

    def accelereaza_masina(self, valoare_accelerare):
        if self.viteza_curenta + valoare_accelerare < self.viteza_maxima:
            self.viteza_curenta += valoare_accelerare
            print(f"Acceleram cu {valoare_accelerare} km/h. Viteza: {self.viteza_curenta} km/h")
        else:
            self.viteza_curenta = self.viteza_maxima
            print(f"Ati atins viteza maxima. Viteza: {self.viteza_curenta} km/h")

    def decelereaza_masina(self, valoare_decelerare):
        if self.viteza_curenta - valoare_decelerare >= 0:
            self.viteza_curenta -= valoare_decelerare
            print(f"Am decelerat cu {valoare_decelerare} km/h. Viteza: {self.viteza_curenta} km/h")
        else:
            self.viteza_curenta = 0
            print(f"Ati atins viteza minima. Viteza: {self.viteza_curenta} km/h")

    def opreste_masina(self):
        self.este_pornita = False
        self.viteza_curenta = 0
        print("Am oprit masina")

    def descrie(self):
        print(f"Marca: {self.marca}")
        print(f"Model: {self.model}")
        print(f"Culoare: {self.culoare}")

    @staticmethod  # metoda statica (fara self) - se poate accesa fara a crea un obiect de tip Masina
    def claxoneaza():
        print("tiit tiiiit")




if __name__ == "__main__":
    toyota = Masina("Toyota", "Auris", "Albastru")
    # toyota.marca = "Toyota"

    bmw = Masina("BMW", "x5", "negru")
    bmw.marca = "BMW"

    numar = 5

    print(type(numar))
    print(type(toyota))
    print(type(bmw))

    # assert bmw == toyota

    print(f"Masina toyota are marca {toyota.marca}")

    audi = Masina("Audi", "A3", "rosu")
    # audi.marca = "Audi"
    print(f"Masina audi are marca {audi.marca}")

    toyota.porneste_masina()
    audi.porneste_masina()

    audi.accelereaza_masina(10)
    audi.claxoneaza()

    # toyota.model = "Auris"
    toyota.an_fabricatie = "2013"
    # toyota.culoare = "Albastru"

    print("---------------------")
    audi.descriere()

    print("---------------------")
    toyota.descriere()
    print("---------------------")
    toyota.accelereaza_masina(5)
    toyota.accelereaza_masina(10)
    toyota.accelereaza_masina(15)
    toyota.accelereaza_masina(30)

    print("---------------------")
    toyota.opreste_masina()
    print(f"Este pornita? {toyota.este_pornita}")

    toyota.porneste_masina()
    toyota.accelereaza_masina(5)

    print(f"Este pornita? {toyota.este_pornita}")
    print("---------------------")

    toyota.accelereaza_masina(200)
    toyota.accelereaza_masina(40)
    toyota.accelereaza_masina(10)
    toyota.accelereaza_masina(50)


    toyota.decelereaza_masina(10)
    toyota.decelereaza_masina(200)
    toyota.decelereaza_masina(30)
    toyota.decelereaza_masina(50)

    toyota.claxoneaza()
    Masina.claxoneaza()

print("Cod in afara if-ului din fisierul cu masina")
print("--------------------------------------------")


