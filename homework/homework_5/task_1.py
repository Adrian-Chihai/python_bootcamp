# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.
number = 4

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.
if number > 0:
    print("number is positive")
else:
    print("number is negative")

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.
# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.
print("par") if number % 2 == 0 else print("impar")

# Creați o variabilă text și atribuiți-i un șir de caractere.
text = "sir de caractere pythonasa"

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
if "python" in text:
    print("exista")
else:
    print("nu exista")

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.
if "Java" in text:
    print("exista")
else:
    print("nu exista")


# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.
if "python" in text:
    print("exista python")
elif "Java" in text:
    print("exista java")
else:
    print("nu exista nimic")

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.
if "python" and "java" in text:
    print("exista ambele")
elif "python" or "java" in text:
    print("exista cel putin unul")
else:
    print("nu exista nimic")

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"

numar = input("Introdu un numar de la 1 la 5: ")

numar = int(numar)
match numar:
    case 1:
        print("Unu")
    case 2:
        print("Doi")
    case 3:
        print("Trei")
    case 4:
        print("Patru")
    case 5:
        print("Cinci")
    case _:
        print("Numar necunoscut")

