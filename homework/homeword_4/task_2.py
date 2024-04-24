# Aceasta este a doua ta sarcină legată de seturi

# Creați un set gol numit `numbers_set`
numbers_set = set()

# Acum adăugați numerele de la 1 la 5 în setul `numbers_set`
for i in range(1, 6):
    numbers_set.add(i)

# Acum afișați setul `numbers_set`
print(numbers_set)

# Acum adăugați numărul 6 la setul `numbers_set`
numbers_set.add(6)

# Acum adaugă numerele de la 1 la 5 în setul `numbers_set` folosind metoda update()
numbers_set.update({1,2,3,4,5})

# Extrageți numărul 3 din setul `numbers_set`
numbers_set.discard(3)

# Ștergeți un număr inexistent din setul `numbers_set` fără a genera o eroare
numbers_set.discard(34)

# Verificați dacă numărul 3 există în setul `numbers_set`
if 3 in numbers_set:
    print("Has number 3")

# Verificați elementele comune din setul `numbers_set` și setul {4, 5, 6, 7}
number_set_1 = set({4,5,6,7})
print(numbers_set.intersection(number_set_1))

# Verificați elementele diferite din setul `numbers_set` și setul {4, 5, 6, 7}
print(numbers_set.difference(number_set_1))

# Verificați dacă setul `numbers_set` este un subset al setului {1, 2, 3, 4, 5, 6, 7}
numbers_set_2 = set({1,2,3,4,5,6,7})
print(numbers_set.issubset(numbers_set_2))

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un subset al setului `numbers_set`
print(numbers_set_2.issubset(numbers_set))

# Verificați dacă setul `numbers_set` este un superset al setului {1, 2, 3, 4, 5, 6, 7}
print(numbers_set.issuperset(numbers_set_2))

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un superset al setului `numbers_set`
print(numbers_set_2.issuperset(numbers_set))

# Afișați lungimea setului `numbers_set`
print(len(numbers_set))

# Ștergeți toate elementele din setul `numbers_set`
numbers_set.clear()

# Afișați setul `numbers_set` pentru a verifica dacă a fost șters
print(numbers_set)

# Asta a fost tot pentru a doua ta sarcină legată de seturi