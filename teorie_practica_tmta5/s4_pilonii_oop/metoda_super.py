from abc import ABC, abstractmethod


class Gradinita(ABC):

    @abstractmethod
    def activitate_practica(self):
        print("Copii se joaca")

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError("Nu ai implementat metoda")


class GradinitaAlbastra(Gradinita):

    def activitate_practica(self):
        super().activitate_practica()
        print("Copiii se joaca din nou")

    def ora_de_somn(self):
        super().ora_de_somn()


gradinita = GradinitaAlbastra()
gradinita.activitate_practica()
