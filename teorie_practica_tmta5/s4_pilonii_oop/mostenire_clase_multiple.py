import time


class Device:
    este_electronic = False

    def pornire_device(self):
        print("Device-ul a pornit")


class Ceas:
    este_digital = False

    def arata_ceasul(self):
        print(time.time())


class CeasDigital(Device, Ceas):
    pass


# Observam cum ceas_digital1 are acces la proprietatile si metodele din ambele clase din care mosteneste
ceas_digital1 = CeasDigital()
ceas_digital1.arata_ceasul()
ceas_digital1.pornire_device()
print(ceas_digital1.este_digital)
print(ceas_digital1.este_electronic)
