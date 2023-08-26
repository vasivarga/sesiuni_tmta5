Feature: Home Page verification
  #Background ne lasa sa scriem o singura data passi care sunt comuni in mai multe scenarii
  #ei vor rula in fundal pentru fiecare scenario, astfel facem economie de cod
  # Pasii din "Given" si "When" daca sunt comuni pot fi folositi in Background

  Background: #pas rulat in fundal
    Given You are on the sign up page

  #Scenario Outline este folosit pentru o organizare mai buna a unui scenariu repetitiv
  # de exemplu cand facem o serie de teste pe un formular de inscriere
  #pentru a verifica campuri obligatorii sau pentru a face validari pe campuri
  #validari in functie de tipuri de caractere acceptate si numar de caractere
  #        equivalence testing and limit boundary testing

  #scenariu repetitiv
  Scenario Outline: I am trying to sign up with invalid fields
    # pas de actiune cu parametri preluati din tabel
    When I fill in the form "<name>", "<email>"
    # pas de rezultat cu parametru preluat din tabel
    Then I receive error message "<error_message>"
    # tabelul cu parametrii pentru fiecare scenariu
    # fiecare rand reprezinta un alt test
    # cu N/A notam pentru a lasa un camp gol
    # mesajele de eroare sunt relative si create de catre noi
    # am folosit urlul care se schimba in cazul in care crearea contului a fost cu success
    # in functie de URL returnam un mesaj de eroare sau altul
    Examples:
      |name    |email           |error_message                       |
      |N/A     |test@google.com |signup not allowed with empty fields|
      |Marian  |N/A             |signup not allowed with empty fields|
      |Marian  |test.google.com |incorrect_email_format              |
      |Marian  |test@google.com |Success                             |
