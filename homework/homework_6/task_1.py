# Aceasta este tema pentru lecția 8 legată de loops
import math
import random
from math import sqrt

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().
list_1 = []
for i in range(11):
    list_1.append(i)

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.
print("for")
for i in range(len(list_1)):
    if list_1[i] % 2 == 0:
        print(list_1[i])

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o
# până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.
print("while")
i = 1
while i <= 5:
    print(i)
    i += 1

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.
print("dictionar")
person = {
    "name": "Ion",
    "age": 22,
    "city": "Chisinau"
}

for k, v in person.items():
    print(f"{k}: {v}")

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.
print("matrix")
matrix = [[2, 3, 5], [3, 6, 8], [9, 5, 5]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.
list_2 = list(range(3, 15))

for i in range(len(list_2)):
    print(list_2[i], end=" ")
print()
# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.
enum_list_2 = list(enumerate(list_2))
print(enum_list_2)

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.
zip_lists = zip(list_1, list_2)
print(list(zip_lists))

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().
list_3 = []

for i in range(1, 11):
    list_3.append(i)

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.
while list_3[0] <= 50:
    for i in range(len(list_3)):
        list_3[i] *= 2

print(list_3)

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].
list_perfect_square = []

for i in range(1, 100):
    if sqrt(i).is_integer():
        list_perfect_square.append(i)

print(list_perfect_square)

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.
list_multiplication = []

for i in range(1, 11):
    list_multiplication.append(7 * i)

print(list_multiplication)

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.
list_of_list = []

for i in range(1, 6):
    sub_list = []
    for j in range(1, 6):
        sub_list.append((i, j))
    list_of_list.append(sub_list)

print(list_of_list)

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .
for row in list_of_list:
    for pair in row:
        i, j = pair
        if i < j:
            print(i, j)

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".
list_rand = [random.randint(1, 25) for _ in range(30)]
print(list_rand)

for i in list_rand:
    if i > 10:
        print(f"la pozitia {list_rand.index(i)} se afla {i} care e mai mare ca 10")
        break
    elif list_rand.index(i) == len(list_rand) - 1:
        print("Nu există valori mai mari decât 10")

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

nr_rows = input("Introdu nr de randuri: ")
nr_col = input("Introdu nr de coloane: ")

for i in range(int(nr_rows)):
    for j in range(int(nr_col)):
        print("*", end=" ")
    print()

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

for i in range(int(nr_rows) + 1):
    for j in range(i):
        print(j + 1, end="")
    print()

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

print()
for i in range(int(nr_rows), 0, -1):
    for j in range(int(nr_rows), int(nr_rows) - i, -1):
        print(j, end="")
    print()

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

chr_start = input("Introdu un caracter de start: ")
chr_end = input("Introdu un caracter de sfarsit: ")

print(ord(chr_start))
print(ord(chr_end))

if ord(chr_start) > ord(chr_end):
    print("Date invalide")
else:
    for i in range(ord(chr_start), ord(chr_end) + 1):
        for j in range(i, ord(chr_end) + 1):
            print(chr(j), end="")
        print()

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

for i in range(int(nr_rows)):
    for j in range(int(nr_col)):
        if i % 2 == 0:
            if j % 2 == 0:
                print("+", end="")
            else:
                print("-", end="")
        else:
            if j % 2 == 0:
                print("-", end="")
            else:
                print("+", end="")
    print()

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

number = input("Introdu un nr: ")
max_pow = input("Introdu puterea maxima: ")

for i in range(int(max_pow) * 2):
    if i <= int(max_pow):
        for j in range(1, int(i) + 1):
            print(math.pow(int(number), j), end=" ")
    else:
        # print(f"start = {i - int(max_pow)}")
        # print(f"end = {max_pow + 1}")
        for j in range(i - int(max_pow) + 1, int(max_pow) + 1):
            print(math.pow(int(number), j), end=" ")
    print()

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
