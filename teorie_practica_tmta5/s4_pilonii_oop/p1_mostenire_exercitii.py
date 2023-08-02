from s4_pilonii_oop.p1_mostenire_clase import AndroidPhone, Iphone

# instantierea unui obiect din clasa AndroidPhone
samsung_galaxy = AndroidPhone("Samsung Galaxy 21", "6.7''", 2020)

# afisam tipul obiectului onePlus8Pro
print(f'Tipul obiectului samsung_galaxy: {type(samsung_galaxy)}')

# apelam metoda turn_on() mostenita din clasa Phone
samsung_galaxy.turn_on()

#observam comportamentul diferit la a a doua apelare (telefonul este deja pornit)
samsung_galaxy.turn_on()

# accesam proprietatea (atributul / field-ul) <<turned_on>> mostenita din clasa Phone
print(f"Este pornit telefonul? >> {samsung_galaxy.turned_on}")

# Incercam sa afisam versiunea de android inainte ca aceasta sa fie setata
# Observam mesajul returnat
samsung_galaxy.print_android_version()

# accesam metoda <<set_android_version()>> mostenita din clasa AndroidPhone pentru a seta versiunea de Android
samsung_galaxy.set_android_version("13")

print(f'Versiunea de Android este {samsung_galaxy.android_version}')
samsung_galaxy.print_android_version()

samsung_galaxy.ring()

samsung_galaxy.print_phone_properties()

# eroare: samsung_galaxy este de tipul AndroidPhone => nu poate accesa print_ios_version()
# samsung_galaxy.print_ios_version()

print("---------------------------------------------------------")


# instantierea unui obiect din clasa Iphone 13 Pro
iphone13pro = Iphone("Iphone 13 PRO", "6''", 2022)

# accesam metoda print_phone_properties() mostenita din clasa Phone
iphone13pro.print_phone_properties()

# Incercam sa afisam versiunea de IOs inainte ca aceasta sa fie setata
# Observam mesajul returnat
iphone13pro.print_ios_version()

# accesam metoda set_ios_version() mostenita din clasa IPhone pentru a seta versiunea de IOs
iphone13pro.set_ios_version(14.0)

# accesam metoda print_ios_version() mostenita din clasa IPhone
iphone13pro.print_ios_version()
