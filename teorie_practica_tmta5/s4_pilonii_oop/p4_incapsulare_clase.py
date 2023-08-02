"""
Incapsulare = restrictionarea accesului la anumite atribute (proprietati/field-uri) sau metode (functii)

Incapsularea se face prin intermediul unor proprietati care poarta numele de modificatori de acces:

Modificatorii de acces sunt Private, Protected, Public

- private = atributul sau metoda definite intr-o clasa sunt vizibile doar in clasa respectiva

- protected = atributul sau metoda pot fi utilizate in afara clasei
    printr-un obiect instantiat din clasa respectiva,
    dar acel atribut sau metoda nu va fi sugerat utilizatorului

- public = atributul sau metoda pot fi utilizate oriunde in afara clasei, si ca vor fi sugerate
    utilizatorului la momentul instantierii obiectului

 Note importante:
 1. In java modificatorii de acces sunt specificati in mod explicit
 prin keyword-urile corespunzatoare: public, private, protected

 In python modificatorii de acces sunt specificati in mod indirect in felul urmator:
 - atributele sau metodele public vor fi definite ca atare fara niciun artificiu
 - atributele sau metodele protected for fi precedate de caracterul "_"
 - atributele sau metodele private for fi precedate de dublu "__"

 2. In python atributul/metoda protected pot fi accesate oriunde, dar ele nu vor fi sugerate utilizatorului la scriere
 In java atributul sau metoda protected vor fi accesate doar in acelasi pachet in care se afla clasa
 """


class User:
    __email = None
    __password = None

    def set_email(self, value):
        if "@" in value and ".com" in value:
            self.__email = value
            print(f"Emailul <<{value}>> a fost salvat cu succes!")
        else:
            print("Emailul nu a fost setat. Formatul este invalid. Reincercati")

    def get_email(self):
        return self.__email

    def delete_email(self):
        self.__email = None


class UserPython:
    __email = None
    __password = None

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @email.setter
    def email(self, value):
        if "@" in value and ".com" in value:
            self.__email = value
            print(f"Emailul <<{value}>> a fost salvat cu succes!")
        else:
            print("Emailul nu a fost setat. Formatul este invalid. Reincercati")

    @email.getter
    def email(self):
        return self.__email
