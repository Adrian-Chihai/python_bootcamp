# Aceeasta este prima sarcină a aceestei lecții și este legată de dicționare.

# Creați un dicțioar gol
dict_1 = {}

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "name" și valoarea fiind "John"
dict_1["name"] = "Jhon"

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "age" și valoarea fiind 30
dict_1["age"] = 30

# Acum afișați dicționarul
print(dict_1)

# Acum ștergeți cheia "name" din dicționar
dict_1.pop("name")

# Acum afișați dicționarul
print(dict_1)

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "city" și valoarea fiind "New York" folosind metoda setdefault()
dict_1["city"] = "New York"

# Afișați toate cheile din dicționar
print(dict_1.keys())

# Afișați toate valorile din dicționar
print(dict_1.values())

# Afișați toate perechile de cheie-valoare din dicționar folosind metoda items()
print(dict_1.items())

# Afișați numărul de perechi de cheie-valoare din dicționar
print(len(dict_1))

# Extrageți valoarea unei chei inexistente fără a genera o eroare
print(dict_1.get("aer"))

# Acum actualizați dicționarul cu un alt dicționar, folosind metoda update()
dict_2 = {"work": "mechanic"}

dict_1.update(dict_2)
print(dict_1)

# Setați valoarea cheii "pizza" la 10 folosind metoda setdefault()
dict_1.setdefault("pizza", 10)

# Afișați dicționarul
print(dict_1)

# Ștergeți cheia "pizza" din dicționar folosind metoda pop()
dict_1.pop("pizza")

# Afișați dicționarul
print(dict_1)

# Ștergeți toate perechile de cheie-valoare din dicționar
dict_1.clear()

# Afișați dicționarul
print(dict_1)
# Asta a fost tot, ai terminat prima ta sarcină legată de dicționare