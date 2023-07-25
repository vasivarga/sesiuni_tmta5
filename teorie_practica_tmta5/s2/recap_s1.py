# OPERATORI LOGICI

sunt_angajat = True
sunt_student = True
sunt_somer = False

# or
# and
# not

# or returneaza true daca cel putin unul dintre operanzi este true
print(sunt_angajat or sunt_somer)

# and returneaza true daca toți operanzii sunt true
print(sunt_angajat and sunt_somer)
print(sunt_angajat and sunt_student)

# not ne returneaza inversul unei valori
print(not sunt_angajat)

# prima data se va executa << not >> mereu, apoi << and >>, iar la final << or >>
print(sunt_angajat or sunt_student or sunt_somer)
# TRUE sau TRUE sau FALSE => TRUE

print(sunt_angajat and sunt_somer or sunt_student)
# TRUE si FALSE sau TRUE =>
# prima data se face TRUE si FALSE => FALS | Ramane FALSE sau TRUE => TRUE

print(not sunt_somer and sunt_angajat or sunt_student)
# not FALSE si TRUE sau TRUE =>
# prima data se face not FALSE => TRUE | Ramane TRUE si TRUE sau TRUE => TRUE

# STRUCTURA IF
# este ca un set de reguli in functie de care instruim programul sa ia deciziile corecte
# adica sa execute codul dorit in functie de situatie/rezultate

# IF SIMPLU - se executa doar daca conditia se evalueaza ca fiind TRUE

if sunt_angajat:
    print("Esti angajat!")

if sunt_somer:
    print("Nu esti angajat")

if not sunt_somer:
    print("Nu esti somer")

# IF - ELSE (conditie initiala + alternativa finala)
# Se executa ramura IF daca conditia se evalueaza ca fiind TRUE, altfel se executa ramura ELSE

if sunt_angajat:
    print("DA, esti angajat!")
else:
    print("NU, nu esti angajat")

# IF cu conditie aditionala ELIF
# Poate contine oricate conditii aditionale
# Se executa PRIMA ramura a carei conditii este TRUE
# Daca nu este niciuna adevarata, nu se va executa nimic

if sunt_somer:
    print("Imi pare rau, nu esti angajat")
elif sunt_angajat:
    print("Felicitari, esti angajat")
elif sunt_student:
    print("Bravo, esti student")

a = 2
b = 1
c = 2

if a == b:
    print("a si b sunt egale")
elif b == c:
    print("b este egal cu c")
elif a == c:
    print("a este egal cu c")


# IF cu conditie aditionala ELIF si conditie finala ELSE

if a > c:
    print("a este mai mare decat c")
elif a < c:
    print("a este mai mic decat c")
else:
    print("a este egal cu c")
