# Aceasta este a treia ta sarcină legată de numere în python
# Creează o variabilă numită `number` și atribuie-i valoarea `10`
number = 10

# Acum afișează valoarea variabilei `number` folosind funcția `print`
print(f"{number}")

# Acum creează o nouă variabilă numită `number2` și atribuie-i valoarea `number` și afișează valoarea variabilei `number2` folosind funcția `print`
number2 = number
print(f"{number2}")

# Acum creează o nouă variabilă numită `number3` și atribuie-i valoarea `4`
number3 = 4

# Acum aplică toate operațiile pe care le-ai învățat în lecție asupra variabilelor `number` și `number3` și afișează rezultatele folosind funcția `print`
# Operațiile sunt: adunare, scădere, înmulțire, împărțire, modulo, exponențiere, împărțire întreagă
print(f"scadere -> {number - number3}")
print(f"adunare -> {number2 + number3}")
print(f"inmultire -> {number3 * number3}")
print(f"impartire -> {number / number3}")
print(f"modulo -> {number % number3}")
print(f"exponentiere -> {pow(number3, number)}")
print(f"impartire intreaga -> {number // number3}")

# Creează o nouă variabilă numită `number4` și atribuie-i o valoare numerică mare într-un mod literal
number4 = 2_350_000

# Acum afișează tipul variabilei `number4` folosind funcția `print`
print(number4)

# Creați o variabilă `numar` și atribuiții valoarea 5.0
numar = 5.0

# Acum afișați tipul lui `numar` folosind funcția `print`
print(type(numar))

# Acum creați o variabilă `numar2` și atribuiții valoarea 2.0
numar2 = 2.0

# Acum creați o variabila `numar_mare` și atribuiți-i o valoare mare utilizând numerele literale
numar_mare = 2_340_450

# Acum afișați tipul lui `numar_mare` folosind funcția `print`
print(type(numar_mare))

# Acum ștergeți variabila `numar_mare` folosind instrucțiunea `del`
del numar_mare
