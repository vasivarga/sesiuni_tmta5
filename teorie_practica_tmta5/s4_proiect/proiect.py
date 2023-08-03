from abc import ABC, abstractmethod


# Recap:
# Decorator = o funcție specială care permite modificarea comportamentului sau aspectului unei alte funcții sau metode.


class Gradinita(ABC):
    # def __init__(self):
    #     self.info_elevi = {}

    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError("Nu ai implementat metoda")


class GradinitaPublica(Gradinita):

    def activitate_practica(self):
        print("Copiii invata sa deseneze")

    def ora_de_somn(self):
        print("Copiii trebuie sa doarma la ora 5")


class GradinitaPrivata(Gradinita):

    def activitate_practica(self):
        print("Copiii invata invata sa modeleze cu plastilina")

    def ora_de_somn(self):
        print("Copii trebuie sa doarma la ora 3")


class GradinitaPublica25(GradinitaPublica):
    info_elevi = {}
    _adresa = "Strada Primaverii 25"
    __director = "Constntin Popoviciu"

    @property
    def director(self):
        return self.__director

    @director.getter
    def director(self):
        return self.__director

    @director.setter
    # Fortam userul sa introduca si nume si prenume numarand cate cuvinte contine numele introdus
    def director(self, nume):
        lungime_nume_director = len(str(nume).split())
        if lungime_nume_director >= 2:
            self.__director = nume
            print("Numele directorului a fost actualizat")
        else:
            print("Trebuie sa introduceti numele complet (nume + prenume)")

    @director.deleter
    def director(self):
        self.__director = None

    def activitate_practica(self):
        # super().activitate_practica()
        print("Copiii se joaca in curte pe balansoar")

    def media_buline_rosii(self, *args):
        suma = 0
        for arg in args:
            suma += arg

        numar_elevi = len(args)

        media = suma / numar_elevi

        if media > 5:
            print("Elevii acestei gradinite sunt foarte neastamparati")
        else:
            print("Elevii acestei gradinite sunt foarte linistiti")

    def media_buline_rosii_tastatura(self):
        lista_cifre = input("Introduceti numerele de buline rosii separte prin virgula: ").split(",")

        lista_numere_intregi = list()

        for numar in lista_cifre:
            lista_numere_intregi.append(int(numar))

        self.media_buline_rosii(*lista_numere_intregi)

    def afisare_elevi(self):
        for key, value in self.info_elevi.items():
            print(f"Elev: {key}")
            print(f"Nume mama: {value['nume_mama']}")
            print(f"Nume tata: {value['nume_tata']}")
            print(f"Varsta: {value['varsta_elev']}")
            print(f"Activitate preferata: {value['activitate_preferata']}")
            print("---------------------------------------------------")

    def inserare_elev(self):
        lista_informatii = input("Introduceti pe rand urmatoarele (separate prin virgula):\n"
                                 "Nume elev,\n"
                                 "Nume mama,\n"
                                 "Nume tata,\n"
                                 "Varsta elev,\n"
                                 "Activitatea preferata\n").split(",")

        # print(lista_informatii)

        nume_elev = lista_informatii[0]
        nume_mama = lista_informatii[1]
        nume_tata = lista_informatii[2]
        varsta_elev = lista_informatii[3]
        activitate_preferata = lista_informatii[4]

        detalii_elev = {
            "nume_mama": nume_mama,
            "nume_tata": nume_tata,
            "varsta_elev": varsta_elev,
            "activitate_preferata": activitate_preferata
        }

        # self.info_elevi.update({"cheie" : "valoare"})
        self.info_elevi.update({nume_elev: detalii_elev})

gradinita_nr1 = GradinitaPublica()
gradinita_nr1.activitate_practica()

gradinita_nr3 = GradinitaPublica()
gradinita_nr3.activitate_practica()

gradinita_nr10 = GradinitaPrivata()
gradinita_nr10.activitate_practica()

print("-----------------------------")
gradinita_nr25 = GradinitaPublica25()
gradinita_nr25.activitate_practica()
gradinita_nr25.ora_de_somn()

gradinita_nr25.media_buline_rosii(4, 3, 5, 4)
gradinita_nr25.media_buline_rosii(5, 5, 5)
gradinita_nr25.media_buline_rosii(5, 5, 5, 10, 5, 4, 20, 30)

# gradinita_nr25.media_buline_rosii_tastatura()


print("-----------------------------")

# Inserarea elevilor se face cu virgula intre valori!!!
# gradinita_nr25.inserare_elev()
# gradinita_nr25.inserare_elev()
gradinita_nr25.afisare_elevi()

print("-----------------------------")
print(gradinita_nr25.info_elevi)
print(gradinita_nr25._adresa)
print(gradinita_nr25.director)

# Setam proprietatea __director cu setter
# La prima incercare ni se afiseaza un mesaj ca numele nu este complet
gradinita_nr25.director = "Ioan"

# La a doua incercare ni se afiseaza un mesaj de succes
gradinita_nr25.director = "Ioan Ardelean"

# Afisam proprietatea __director cu getter
print(gradinita_nr25.director)

# Stergem proprietatea __director cu deleter
del gradinita_nr25.director

print(gradinita_nr25.director)
