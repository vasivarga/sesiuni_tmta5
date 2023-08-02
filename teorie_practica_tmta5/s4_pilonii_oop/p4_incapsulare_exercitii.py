from s4_pilonii_oop.p4_incapsulare_clase import UserPython, User

user = User()

# Incercam sa setam email cu format invalid
# Observam ca setterul (metoda set_email) ne impiedica
user.set_email("alabalaportocala")

# Setam email cu format valid
user.set_email("alabalaportocala@yahoo.com")

# Incercam sa accesam proprietatea __email
# Observam ca ne da eroare => comentam codul ca sa putem trece mai departe
# print(user.__email)

# Metoda corecta pentru a accesa proprietatea <<__email>> prin getter (metoda get_email())
print(user.get_email())

user.delete_email()
print(user.get_email())

print("-----------------------")

user = UserPython()
user.email = "alabala"
user.email = "alabala@yahoo.com"

print(user.email)