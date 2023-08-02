from s4_pilonii_oop.p2_abstractizare_clase import Sarpe, Pisica, Animal

# Instantiem un obiect de tip Pisica()
pisica_obiect = Pisica()
pisica_obiect.scoate_sunet()
pisica_obiect.print_proprietati()

# Verificam daca clasa Pisica este o subclasa a clasei Animal (adica daca mosteneste din clasa Animal)
print(f"Clasa <<Pisica>> este o subclasa a clasei <<Animal>>: {issubclass(Pisica, Animal)}")

# Verificam daca obiectul pisica_obiect este o instanta a clasei Animal
print(f"Obiectul <<pisica_obiect>> este o instanta a clasei <<Animal>>: {isinstance(pisica_obiect, Animal)}")

# Verificam daca obiectul pisica_obiect este o instanta a clasei Pisica
print(f"Obiectul <<pisica_obiect>> este o instanta a clasei <<Pisica>>: {isinstance(pisica_obiect, Pisica)}")

print("-----------------------------------")

sarpe_obiect = Sarpe()
sarpe_obiect.scoate_sunet()
sarpe_obiect.print_proprietati()

# Verificam daca clasa Sarpe este o subclasa a clasei Animal (adica daca mosteneste din clasa Animal)
print(f"Clasa <<Sarpe>> este o subclasa a clasei <<Animal>>: {issubclass(Sarpe, Animal)}")

# Verificam daca obiectul sarpe_obiect este o instanta a clasei Animal
print(f"Obiectul <<sarpe_obiect>> este o instanta a clasei <<Animal>>: {isinstance(sarpe_obiect, Animal)}")

# Verificam daca obiectul sarpe_obiect este o instanta a clasei Sarpe
print(f"Obiectul <<sarpe_obiect>> este o instanta a clasei <<Sarpe>>: {isinstance(sarpe_obiect, Sarpe)}")

# Verificam daca clasa Sarpe este o subclasa a clasei Pisica (adica daca mosteneste din clasa Pisica)
print(f"Clasa <<Sarpe>> este o subclasa a clasei <<Animal>>: {issubclass(Sarpe, Pisica)}")
