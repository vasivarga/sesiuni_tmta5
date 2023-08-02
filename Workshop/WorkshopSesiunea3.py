# def suma(*args):
#     suma  = 0
#     for arg in args:
#         suma = suma + arg
#     return suma
#
# print(suma(3,7))    practica functii cu multiple args

class Cinema:
    nume = "Iulius"
    adresa = "Calea Victoriei nr 20"
    nr_sali = 5
    nr_locuri_sala = 20
    snack_bar = True
    case_bilete_deschise = None
    nr_angajati = 20
    ora_curenta = "16:00"
    orar = "Z:Luni-Duminica/ H:14:00 - 24:00"
    nr_filme_2D = 10
    nr_filme_3D = 15
    numar_bilete_vandute = 70
    tip_client = "adult"
    pret_bilet = 20

   # daca ora curenta este mai mica de 19:00 atunci nr case <=2  else >2 <=4
    def __init__(self, ora_curenta, case_bilete_deschise):
        self.ora_curenta = ora_curenta
        if int(ora_curenta[0:2]) <= 19 and case_bilete_deschise > 2:
            print("In timpul programului de zi, sunt deschise maxim 2 case")
        elif int(ora_curenta[0:2]) <= 19 and case_bilete_deschise < 1:
            print("Trebuie minim o casa deschisa")
        elif int(ora_curenta[0:2]) <= 19 and case_bilete_deschise <=2:
            self.case_bilete_deschise = case_bilete_deschise
        elif int(ora_curenta[0:2]) > 19 and case_bilete_deschise < 2:
            print("In timpul programului de seara, sunt deschise minim 2 case")
        elif int(ora_curenta[0:2]) > 19 and case_bilete_deschise > 4:
            print("Nu avem mai mult de 4 case disponibile")
        else:
            self.case_bilete_deschise = case_bilete_deschise


    # daca esti student ai reducere 10% copii 50%, seniori 30%
    def calcul_pret(self, tip_client, pret_bilet):
        self.tip_client = tip_client
        if tip_client == "student":
            self.pret_bilet = int(pret_bilet) * 0.9
        elif tip_client == "copil":
            self.pret_bilet = int(pret_bilet)/2
        elif tip_client == "senior":
            self.pret_bilet = int(pret_bilet) * 0.7
        elif tip_client == "adult":
            self.pret_bilet = pret_bilet
        else:
            print("tip client neacceptat")
        return self.pret_bilet


    def numar_case(self):
        print(self.case_bilete_deschise)

# class Cinema:
#     nume = None
#     adresa = None
#     nr_sali = None
#     nr_locuri_sala = None
#     snack_bar = None
#     case_bilete_deschise = None
#     nr_angajati = None
#     orar = None
#     nr_filme_2D = None
#     nr_filme_3D = None
#     numar_bilete_vandute = None


    # def __init__(self, nume, nr_sali, nr_locuri_sala, numar_bilete_vandute):
    #     self.nume = nume
    #     self.nr_sali = nr_sali
    #     self.nr_locuri_sala = nr_locuri_sala
    #     self.numar_bilete_vandute = numar_bilete_vandute


#intre 4 si 8 caractere si toate vocale
    # def __init__ (self, adresa, snack_bar, nr_locuri_sala, nume):
    #     self.adresa = adresa
    #     self.snack_bar = snack_bar
    #     if nr_locuri_sala < 1 or nr_locuri_sala > 100:
    #         print("Sala trebuie sa aiba intre 1 si 100 de locuri")
    #     else:
    #         self.nr_locuri_sala = nr_locuri_sala
    #     #lista_vocale = ["A","E","I","O","U"]
    #     lista_vocale = "aeiou"
    #     vocala = True
    #     if len(nume) < 4 or len(nume) > 8:
    #         print('Numele cinemaului trebuie sa aiba intre 4 si 8 caractere')
    #     else:
    #         for i in range(0, len(nume)):
    #             #if nume[i].upper() not in lista_vocale:
    #             if nume[i].lower() not in lista_vocale:
    #                 vocala = False
    #                 break
    #         if vocala:
    #             self.nume = nume
    #         else:
    #             print("Numele cinemaului trebuie sa contina doar vocale")


    # def print_nr_case_deschise(self):
    #        print(self.case_bilete_deschise)
    def schimbare_nr_case_deschise(self, case_bilete_deschise):
       self.case_bilete_deschise = case_bilete_deschise


    def calcleaza_numar_total_de_locuri(self, nr_sali, nr_locuri_sala):
        self.nr_sali = nr_sali
        self.nr_locuri_sala = nr_locuri_sala
        nr_total = self.nr_sali * self.nr_locuri_sala
        return nr_total

    #varianta 1 cu valori hardcoded
    # def calculeaza_locuri_libere(self, nr_bilete_vandute ):
    #     nr_total = self.calcleaza_numar_total_de_locuri(5,20)
    #     self.nr_bilete_vandute = nr_bilete_vandute
    #     numar_locuri_libere = nr_total - self.numar_bilete_vandute
    #     return numar_locuri_libere

   #varianta 2 cu 3 parametri
    # def calculeaza_locuri_libere(self, nr_bilete_vandute, nr_sali, nr_locuri_sala ):
    #     self.nr_bilete_vandute = nr_bilete_vandute
    #     self.nr_sali = nr_sali
    #     self.nr_locuri_sala = nr_locuri_sala
    #     nr_total = self.nr_sali * self.nr_locuri_sala
    #     numar_locuri_libere = nr_total - self.numar_bilete_vandute
    #     return numar_locuri_libere

    #varianta 3
    def calculeaza_locuri_libere(self):
        nr_total = self.nr_sali * self.nr_locuri_sala
        #numar_locuri_libere = nr_total - self.numar_bilete_vandute
        numar_locuri_libere = (self.nr_sali * self.nr_locuri_sala) - self.numar_bilete_vandute
        return numar_locuri_libere

    def printare_cu_formatare(self):
        print(f'Cinemaul nostru are urmatoarele detalii: ',
              f'Nume Cinema: {self.nume}',
              f'Adresa Cinema: {self.adresa} ',
              f'Numar Sali: {self.nr_sali}',
              f'Numar locuri sala: {self.nr_locuri_sala}',
              f'Snack bar: {self.snack_bar}',
              f'Numar Case Bilete: {self.case_bilete_deschise}',
              f'Numar angajati: {self.nr_angajati}',
              f'Orar: {self.orar}',
              f'Numar filme 2D: {self.nr_filme_2D}',
              f'Numar filme 3D: {self.nr_filme_3D}',
              f'Numar bilete vandute: {self.numar_bilete_vandute}',
              sep = "\n"
              )
    def pritare_lista(self):
        lista = [self.nume, self.numar_bilete_vandute, self.nr_filme_3D]
        print(lista)

    def printare_nume(self):
        print(self.nume)
    def printare_lista_cu_formatare(self):
        lista = [f'Nume Cinema: {self.nume}',
              f'Adresa Cinema: {self.adresa} ',
              f'Numar Sali: {self.nr_sali}',
              f'Numar locuri sala: {self.nr_locuri_sala}',
              f'Snack bar: {self.snack_bar}',
              f'Numar Case Bilete: {self.case_bilete_deschise}',
              f'Numar angajati: {self.nr_angajati}',
              f'Orar: {self.orar}',
              f'Numar filme 2D: {self.nr_filme_2D}',
              f'Numar filme 3D: {self.nr_filme_3D}',
              f'Numar bilete vandute: {self.numar_bilete_vandute}']

        for i in range(0, len(lista)):
            print(lista[i])

        print('###############################################################')

        j = 0
        while j < len(lista):
            print(lista[j])
            j += 1

        print('#################################################################')

        for element in lista:
            print(f'Elementul curent este: {element}')



# cinema1 = Cinema("Iulius", 4, 25, 63)
# cinema2 = Cinema("Vivo", 6, 30, 100)
# cinema1.print_nr_case_deschise()
# cinema1.schimbare_nr_case_deschise(6)
# cinema1.print_nr_case_deschise()
# numar_total_locuri = cinema1.calcleaza_numar_total_de_locuri(5,20)
# #numar_locuri_libere = numar_total_locuri - 70
# print(numar_total_locuri)
# #print(numar_locuri_libere)
# #nr_locuri_libere = cinema1.calculeaza_locuri_libere(70)...........V1
# #nr_locuri_libere = cinema1.calculeaza_locuri_libere(70, 5, 20).........V2
# nr_locuri_libere = cinema1.calculeaza_locuri_libere()
# print(nr_locuri_libere)
# print(cinema1.calculeaza_locuri_libere())
# print(cinema2.calculeaza_locuri_libere())
# cinema1 = Cinema()
# cinema1.printare_cu_formatare()
# cinema1.pritare_lista()
# cinema1.printare_lista_cu_formatare()

# cinema1 = Cinema("Strada Lalelelor", False, 90, "aEaIaaaaaaa")
# cinema1.printare_nume()

cinema2 = Cinema("20:00", 4)
pret_bilet = cinema2.calcul_pret("caine", 10)
print(pret_bilet)