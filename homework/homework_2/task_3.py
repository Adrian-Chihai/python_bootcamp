# Aceasta este a treia ta sarcină a lecției legată de type conversion și input-ul user-ului în python

# Creează o variabilă numită `number` și atribuie-i valoarea `10`
number = '10'

# Acum afișează valoarea variabilei `number` folosind funcția `print`
print(f"{number}")

# Acum cere user-ului să introducă un număr și atribuie acea valoare variabilei `number` și afișeaz-o folosind funcția `print`
number = input("Enter a number: ")

# Acum afișează tipul variabilei `number` folosind funcția `print`
print(number)

# Convertește variabila `number` la tipul `float` și afișează tipul variabilei `number` folosind funcția `print`
number = float(number)
print(type(number))

# Convertește variabila `number` la tipul `str` și afișează tipul variabilei `number` folosind funcția `print`
number = str(number)
print(type(number))

# Convertește variabila `number` la tipul `bool` și afișează tipul variabilei `number` folosind funcția `print`
number = bool(number)
print(type(number))
# Asta a fost tot pentru această sarcină