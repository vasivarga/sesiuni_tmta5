class Pisica:
    rasa = None
    nume = None
    culoare = None

    def __init__(self, nume):
        self.nume = nume

    def miauna(self):
        print(f"{self.nume} face miau...")

    def toarce(self):
        print(f"{self.nume} face prrrr...")

    def vaneaza(self):
        print(f"{self.nume} a plecat la vanat.")

    def aducere_la_veterinar(self):
        print(f"{self.nume} merge la vet.")