# Aceasta este a doua sarcină legată de tuples

# Creează un tuple numit `numbers` care să conțină numerele de la 1 la 5
numbers = (1, 2, 3, 4, 5)

# Acum afișează tuple `numbers`
print(numbers)

# Acum adaugă numărul 6 la tuple `numbers`
numbers = numbers + (6,)

# Acum afișează tuple `numbers`
print(numbers)

# Afișeați primul element din tuple `numbers`
print(numbers[0])

# Afișeați ultimul element din tuple `numbers`
print(numbers[len(numbers) - 1])

# Afișeați primele două elemente din tuple `numbers`
print(numbers[:2])

# Afișeați ultimele două elemente din tuple `numbers`
print(numbers[2:])

# Afișați lungimea tuple `numbers`
print(len(numbers))

# Afișați suma elementelor din tuple `numbers`
print(sum(numbers))

# Schibați elementul de la poziția 2 din tuple `numbers` cu 10
numbers_list = list(numbers)
numbers_list[2] = 10
numbers = tuple[numbers_list]

# Afișați tuple `numbers`
print(numbers)

# Ștergeți tuple `numbers`
del numbers
