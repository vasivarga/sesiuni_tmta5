from abc import ABC, abstractmethod


'''
Presupunem ca se organizeaza competitii la nivel de scoala. 
Implementati solutia pentru competitii in oricare din clase doriti voi, 
incercand sa aplicati si celelalte concepte de mostenire si abstractizare si polimorfism
'''
#olimpiade

class Gradinita(ABC):

    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError("Nu ai implementat metoda")

    @abstractmethod
    def olimpiada(self):
        raise NotImplementedError("Nu sunt olimpiade in scoala")

class G_Private1(Gradinita):
    __detalii_elevi = dict()
    matematicieni = None


    @property
    def detalii_elevi(self):
        return self.__detalii_elevi

    @detalii_elevi.getter
    def detalii_elevi(self):
        return self.__detalii_elevi

    @detalii_elevi.deleter
    def detalii_elevi(self):
        self.__detalii_elevi.clear()

    @detalii_elevi.setter
    def detalii_elevi(self,detalii):
        for key, value in detalii.items():
            if int(value["varsta"]) >= 8:
                print("Prea batran pentru gradinita")
            else:
                self.__detalii_elevi.update(detalii)

    def activitate_practica(self):
        print("Elevii joaca darts ->")

    def ora_de_somn(self):
        print("Copii dorm de la 14:00 la 15:00")


    def olimpiada(self,*args): #(1, 6, 4)
        print("Super olimpiada la matematica")
        self.matematicieni = self.nr_elevi()/2
        print(f'Numar concurenti: {self.matematicieni}')
        numere = len(args)
        suma = 0
        for arg in args:
            suma = suma+int(arg)
        media = suma/numere
        print(f"Media Aritmetica este: {media}")
        print(f'Media a fost calculata cu succes de: {self.matematicieni/2} elevi')

    def _AdaugaElevTst(self):
        valoare_nume = input("Introduceti numele elevului: ")
        varsta = input("Introduceti varsta elevului: ")
        an_inscriere = input("Introduceti anul inscrierii: ")
        # lista_elevi = input("Intoruceti detalii elev:\n"
        #                     "Nume elev,\n"
        #                     "Varsta,\n"
        #                     "Anul inscrierii\n"
        #                     ).split(",")
        # valoare_nume = lista_elevi[0]
        # varsta = lista_elevi[1]
        # an_inscriere = lista_elevi[2]
        dictionarul_mic = {
            "varsta": varsta,
            "an inscriere": an_inscriere
        }
        return {valoare_nume:dictionarul_mic}


    def _AdaugaElevKwa(self, **kwargs):
        for key, value in kwargs.items():
            valoare_nume = key
            varsta = value["varsta"]
            an_inscriere = value["an_inscriere"]
            dictionarul_mic = {
                "varsta": varsta,
                "an inscriere": an_inscriere
            }
            return {valoare_nume:dictionarul_mic}

       #{“valoare_nume”:{“varsta”:”valoare_varsta”, “an_inscriere”:”valoare an inscriere”}}
    # {“Marian”:{“varsta”:”5”, “an_inscriere”:”2021”}}

    def printeaza_elev(self):
        if len(self.__detalii_elevi) >0:
            for key, value in self.detalii_elevi.items():
                print(f'Nume elev: {key}')
                print(f'Varsta elev: {value["varsta"]}')
                print(f'Anul inscrierii: {value["an inscriere"]}')
                print("------------------------------------------------")
        else:
            print("Dictionarul este gol")

    def nr_elevi(self):
        return len(self.__detalii_elevi)


'''
Definiti o metoda in interiorul clasei GradinitaPrivata() care sa se numeasca adauga_elev() si sa primeasca de la tastatura informatii despre elevul care se adauga. 

Functia va implementa polimorfismul prin **kwargs si va primi ca si parametru urmatoarele informatii despre elev:

{“valoare_nume”:{“varsta”:”valoare_varsta”, “an_inscriere”:”valoare an inscriere”}}

Metoda va fi protected si va adauga informatiile cu privire la acel elev intr-un dictionar definit la inceputul clasei si care va fi populat prin intermediul metodei apelate.

Dictionarul definit va fi private si se va accesa prin getter, se va modifica prin setter si se va sterge prin deleter (pe langa metoda de populare de mai sus).

'''
class G_Public(Gradinita):
    __detalii_elevi = dict()
    matematicieni = None
    istorici = None

    @property
    def detalii_elevi(self):
        return self.__detalii_elevi

    @detalii_elevi.getter
    def detalii_elevi(self):
        return self.__detalii_elevi

    @detalii_elevi.deleter
    def detalii_elevi(self):
        self.__detalii_elevi.clear()

    @detalii_elevi.setter
    def detalii_elevi(self,detalii):
        for key, value in detalii.items():
            if int(value["varsta"]) >= 8:
                print("Prea batran pentru gradinita")
            else:
                self.__detalii_elevi.update(detalii)

    def activitate_practica(self):
        print("Elevii joaca darts ->")

    def ora_de_somn(self):
        print("Copii dorm de la 14:00 la 15:00")


    def olimpiada(self,*args):
        print("Super olimpiada la Istorie")
        self.istorici = self.nr_elevi()
        print(f'Numar concurenti: {self.istorici}')
        print("In ce an a inceput al 2-lea razboi mondial ?")
        anul = None
        for arg in args:
            if arg == 1939:
                print("Am raspuns la intrebare")
                anul = arg
                break

        if anul == None:
            print("Nu am gasit raspunsul corect")
            print("Nu avem olimpici")
        else:
            print(f"Raspunsul corect este: {anul}")
            print(f'Au raspuns cu success: {self.istorici/2} elevi')

    def nr_elevi(self):
        return len(self.__detalii_elevi)


gradi1 = G_Private1()
# #gradi1._AdaugaElevKwa(Cerasela={"varsta":6, "an_inscriere":2018})
# #gradi1._AdaugaElevTst()
# gradi1.detalii_elevi = gradi1._AdaugaElevKwa(Cerasela={"varsta":6, "an_inscriere":2018})
# #gradi1.detalii_elevi = gradi1._AdaugaElevTst()
# gradi1.detalii_elevi = {"Georgian":{"varsta":9,"an inscriere":2018}}
# gradi1.printeaza_elev()
# del gradi1.detalii_elevi
# gradi1.printeaza_elev()
#gradi1.nr_elevi()
gradi1.detalii_elevi = {"Georgian":{"varsta":5,"an inscriere":2018}}
gradi1.detalii_elevi = {"Alexandru":{"varsta":4,"an inscriere":2018}}
gradi1.detalii_elevi = {"Marcel":{"varsta":5,"an inscriere":2018}}
gradi1.detalii_elevi = {"Petrica":{"varsta":7,"an inscriere":2018}}
gradi1.olimpiada(1,6,5)
gradi2 = G_Public()
gradi2.detalii_elevi = {"Georgian":{"varsta":5,"an inscriere":2018}}
gradi2.detalii_elevi = {"Alexandru":{"varsta":4,"an inscriere":2018}}
gradi2.detalii_elevi = {"Marcel":{"varsta":5,"an inscriere":2018}}
gradi2.detalii_elevi = {"Petrica":{"varsta":7,"an inscriere":2018}}
gradi2.olimpiada(1918,1929,1048)


