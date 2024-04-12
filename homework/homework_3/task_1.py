# Aceasta este prima ta sarcină legată de liste

# Creează o listă goală numită `numbers`
numbers = []

# Acum adaugă numerele de la 1 la 5 în lista `numbers`
for i in range(5):
    numbers.append(i + 1)


# Acum afișează lista `numbers`
print(numbers)


# Acum adaugă numărul 6 la lista `numbers`
numbers.append(6)

# Acum afișează lista `numbers`
print(numbers)

# Acum șterge numărul 3 din lista `numbers`
numbers.remove(3)

# Acum afișează lista `numbers`
print(numbers)

# Acum sortează lista `numbers`
numbers.sort()

# Acum afișează lista `numbers`
print(numbers)

# Acum inversează lista `numbers`
numbers.reverse()

# Acum afișează lista `numbers`
print(numbers)

# Acum afișează lungimea listei `numbers`
print(len(numbers))

# Acum selectează primele două elemente din lista `numbers` și afișează-le
print(numbers[:2])

# Acum selectează ultimele trei elemente din lista `numbers` și afișează-le
print(numbers[len(numbers) - 3:])

# Acum adaugă numărul 3 la poziția 2 în lista `numbers`
numbers.insert(2, 3)

# Acum afișează lista `numbers`
print(numbers)

# Creează o listă goală numită `numbers2`
numbers2 = []

# Acum adaugă numerele de la 6 la 10 în lista `numbers2`
for i in range(6, 11):
    numbers2.append(i)

# Acum afișează lista `numbers2`
print(numbers2)

# Acum adaugă lista `numbers2` la lista `numbers`
numbers.append(numbers2)

# Acum afișează lista `numbers`
print(numbers)

# Acum transformă lista `numbers` într-un string și afișează-l
str_numbers = str(numbers)
print(type(str_numbers))
print(str_numbers)

# Asta a fost tot, ai terminat prima ta sarcină legată de liste
