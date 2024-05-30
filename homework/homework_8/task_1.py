from functools import reduce

from sigmoid_check.python_odyssey.lesson_11.lesson_11 import Lesson11

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.4
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.4

# VERIFICATION PROCESS
session = Lesson11()
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_1` care poate primi un număr variabil de argumente și returnează suma acestora.
Exemplu: task_1(1, 2, 3) ➞ 6
"""

# CODUL TĂU VINE MAI JOS:
def task_1(*args):
    sum = 0
    for nr in args:
        sum += nr
    return sum
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_1(task_1))
# VERIFICATION PROCESS


"""
Task: Creați o funcție cu numele `task_2` care primește un număr variabil de argumente și returnează o listă cu argumentele care sunt numere întregi.
Exemplu: task_2(1, 2, 'a', 'b') ➞ [1, 2]
"""

# CODUL TĂU VINE MAI JOS:
def task_2(*args):
    int_nr = []
    for nr in args:
        if type(nr) == int:
            int_nr.append(nr)
    return int_nr
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(task_2))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_3` care poate primi un număr variabil de argumente și va returna produsul acesora.
Exemplu: task_3(1, 4, 5) ➞ 20
"""

# CODUL TĂU VINE MAI JOS:
def task_3(*args):
    prod = 1

    for nr in args:
        prod *= nr
    return prod
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(task_3))
# VERIFICATION PROCESS

"""
x   x   
"""

# CODUL TĂU VINE MAI JOS:
def task_4(**kwargs):
    key_values = ""
    for key, value in kwargs.items():
        key_values += f"{key} {value} "
    return key_values.strip()
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_4(task_4))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_5` care primește un număr variabil de argumente și returnează două liste separate.
Prima listă conține toate argumentele de tip întreg sortate în ordine crescătoare, iar a doua listă conține denumirea tuturor argumentelor keyword care sunt de tip string sortate în ordine alfabetică.
Exemplu: task_6(3, 1, 2, a=10, b=20) ➞ [1, 2, 3], []
Exemplu: task_6(3, 1, 2, a=10, b=20, c='a') ➞ [1, 2, 3], ['c']
Exemplu: task_6(3, 1, 2, a=10, b=20, c='a', d='b') ➞ [1, 2, 3], ['c', 'd']
"""

# CODUL TĂU VINE MAI JOS:
def task_5(*args, **kwargs):
    int_list = [arg for arg in args if isinstance(arg, int)]
    int_list.sort()

    str_keys_list = [key for key, value in kwargs.items() if isinstance(value, str)]
    str_keys_list.sort()

    return int_list, str_keys_list
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_5(task_5))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_6` care primește un număr variabil de argumente și returnează un dicționar care conține toate argumentele keyword ca key și valoarea acestora ca value.
Exemplu: task_6(a=1, b=2, c=3) ➞ {'a': 1, 'b': 2, 'c': 3}
"""

# CODUL TĂU VINE MAI JOS:
def task_6(**kwargs):
    created_dict = {}

    for key, val in kwargs.items():
        created_dict[key] = val
    return created_dict
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_6(task_6))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_7` care poate primi un număr nedeterminat de argumente atât string-uri cât și numere și va returna un dicționar cu două chei: `str` și `int`.
Cheia `str` va avea o listă cu toate string-urile primite ca argumente, iar cheia `int` va avea o listă cu toate numerele primite ca argumente.
Exemplu: task_7(1, 'a', 2, 'b') ➞ {'str': ['a', 'b'], 'int': [1, 2]}
"""

# CODUL TĂU VINE MAI JOS:
def task_7(*args):
    data_dict = {'str': None,
                 'int': None
                 }

    list_str = []
    list_int = []
    for val in args:
        if isinstance(val, str):
            list_str.append(val)
        elif isinstance(val, int):
            list_int.append(val)

    data_dict['str'] = list_str
    data_dict['int'] = list_int
    return data_dict
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_7(task_7))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_8` care primește un număr variabil de argumente și returnează un dicționar cu două chei: `palindrom` și `non_palindrom`.
Cheia `palindrom` va avea o listă cu toate argumentele care sunt palindroame, iar cheia `non_palindrom` va avea o listă cu toate argumentele care nu sunt palindroame.
Exemplu: task_8('madam', 'hello', 'level', 'world') ➞ {'palindrom': ['madam', 'level'], 'non_palindrom': ['hello', 'world']}
"""

# CODUL TĂU VINE MAI JOS:
def task_8(*args):
    list_palindrome = ([word for word in args if word == word[::-1]])
    list_non_palindrome = ([word for word in args if word != word[::-1]])

    dictionar = {'palindrom': list_palindrome,
                 'non_palindrom': list_non_palindrome
                 }

    return dictionar
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_8(task_8))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_9` care primește un număr variabil de argumente de tip integer și un argument `number` de tip integer.
Funcția va returna toate argumentele care sunt multipli ai lui `number`.
Exemplu: task_9(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
"""

# CODUL TĂU VINE MAI JOS:
def task_9(*args, number):
    return [num for num in args if num % number == 0]

    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_9(task_9))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_10` care primește un număr variabil de argumente de tip integer și un argument `number` de tip integer.
Funcția va returna toate argumentele care sunt divizibile cu `number`.
Exemplu: task_10(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
"""

# CODUL TĂU VINE MAI JOS:
def task_10(*args, number):
    print([num for num in args if num % number == 0])
    return [num for num in args if num % number == 0]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_10(task_10))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_11` care primește un număr variabil de argumente de tip integer care reprezintă șirul Fibonacci.
Funcția va returna valoarea True dacă șirul Fibonacci este corect și False în caz contrar.
Exemplu: task_11(1, 1, 2, 3, 5, 8) ➞ True
Exemplu: task_11(1, 1, 2, 3, 5, 9) ➞ False
"""

# CODUL TĂU VINE MAI JOS:
def task_11(*args):
    list_args = []

    for nr in args:
        if len(list_args) >= 2:
            if nr != list_args[len(list_args) - 1] + list_args[len(list_args) - 2]:
                return False
        list_args.append(nr)

    if len(list_args) < 2:
        return False

    if len(list_args) == 2:
        return True

    return True
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_11(task_11))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_12` care primește un număr variabil de argumente de tip integer.
Funcția va returna True dacă toate argumentele sunt numere prime și False în caz contrar.
Exemplu: task_12(2, 3, 5, 7) ➞ True
Exemplu: task_12(1, 2, 3, 4) ➞ False
"""

# CODUL TĂU VINE MAI JOS:
def task_12(*args):

    for nr in args:
        if nr <= 1:
            return False
        for i in range(2, int(nr**0.5) + 1):
            if nr % i == 0:
                return False

    return True
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_12(task_12))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_13` care primește obligatoriu un argument de tip string și un număr variabil de argumente de tip string.
Funcția va returna True dacă toate argumentele sunt anagrame și False în caz contrar.
Exemplu: task_13('listen', 'silent') ➞ True
Exemplu: task_13('hello', 'world') ➞ False
"""

# CODUL TĂU VINE MAI JOS:
def task_13(main_str, *args):
    main_str_sorted = ''.join(sorted(main_str))

    for arg in args:
        if ''.join(sorted(arg)) != main_str_sorted:
            return False

    return True
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_13(task_13))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_14` care primește un argument `sub_string` de tip string și un număr variabil de argumente de tip string.
Funcția va returna o listă cu toate argumentele care conțin `sub_string`.
Exemplu: task_14('home', 'same', 'meme', sub_string="me") ➞ ['home', 'meme', 'same']
"""

def task_14(*args, sub_string):
    return [word for word in args if sub_string in word]
    pass
# CODUL TĂU VINE MAI JOS:
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_14(task_14))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_15` care primește un argument `sub_string` de tip string și un număr variabil de argumente de tip string.
Funcția va returna un dicționar cu două chei: `contains` și `not_contains`.
Cheia `contains` va avea o listă cu toate argumentele care conțin `sub_string`, iar cheia `not_contains` va avea o listă cu toate argumentele care nu conțin `sub_string`.
Exemplu: task_15('home', 'same', 'meme', sub_string = 'me') ➞ {'contains': ['home', 'same', 'meme'], 'not_contains': []}
"""

# CODUL TĂU VINE MAI JOS:
def task_15(*args, sub_string):
    list_contains = [word for word in args if sub_string in word]
    list_not_contains = [word for word in args if sub_string not in word]

    return {'contains': list_contains, 'not_contains': list_not_contains}
    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_15(task_15))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_16` care va primi un număr variabil de argumente de tip integer și un argument `ooperation` de tip string.
Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor.
Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
Exemplu: task_16(2, 3, 4, 5, operation='add') ➞ 14
Exemplu: task_16(2, 3, 4, 5, operation='sub') ➞ -10
Exemplu: task_16(2, 3, 4, 5, operation='mul') ➞ 120
Exemplu: task_16(2, 3, 4, 5, operation='div') ➞ 0.008333333333333333
"""

# CODUL TĂU VINE MAI JOS:
def task_16(*args, operation):
    res_add_sub = 0
    res_mul_div = 1
    match operation:
        case 'add':
            return sum(args)
        case  'sub':
            return args[0] - sum(args[1:])
        case 'mul':
            return reduce(lambda x, y: x * y, args)
        case 'div':
            return reduce(lambda x, y: x / y, args)

    pass
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_16(task_16))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_17` care primește un argument `number` după putea primi diferite argumente keyword precum `add`, `sub`, `mul`, `div` care vor fi liste cu numere.
Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor. Mai multe operații pot fi aplicate. Ordinea operațiilor va fi în ordinea în care sunt specificate.
Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
Exemplu: task_17(2, add=[3, 4, 5]) ➞ 14
Exemplu: task_17(2, sub=[3, 4, 5]) ➞ -10
Exemplu: task_17(2, mul=[3, 4, 5]) ➞ 120
Exemplu: task_17(2, div=[3, 4, 5]) ➞ 0.008333333333333333
Exemplu: task_17(2, add=[3, 4, 5], sub=[1, 2]) ➞ 11
"""

# CODUL TĂU VINE MAI JOS:
def task_17(number, **kwargs):
    result = number

    for operation, values in kwargs.items():
        if operation == 'add':
            result += sum(values)
        elif operation == 'sub':
            result -= sum(values)
        elif operation == 'mul':
            for value in values:
                result *= value
        elif operation == 'div':
            for value in values:
                result /= value

    return result
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_17(task_17))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_18` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi caracterele întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale caracterelor.
Exemplu: task_18('hello', 'world') ➞ {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
"""

# CODUL TĂU VINE MAI JOS:
def task_18(*args):
    char_count = {}
    for string in args:
        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_18(task_18))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_19` care primește un număr variabil de argumente de tip integer și va returna un dicționar în care cheile vor fi numerele prime întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale numerelor prime.
Exemplu: task_19(1, 2, 3, 4, 5, 6, 7, 8, 9) ➞ {2: 1, 3: 1, 5: 1, 7: 1}
"""

# CODUL TĂU VINE MAI JOS:
def task_19(*args):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_count = {}
    for num in args:
        if is_prime(num):
            if num in prime_count:
                prime_count[num] += 1
            else:
                prime_count[num] = 1
    return prime_count
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_19(task_19))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_20` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi lungimile cuvintelor întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale lungimilor cuvintelor.
Exemplu: task_20('hello', 'world') ➞ {5: 2}
Exemplu: task_20('hello', 'world', 'python') ➞ {5: 2, 6: 1}
"""

# CODUL TĂU VINE MAI JOS:
def task_20(*args):
    length_count = {}
    for string in args:
        length = len(string)
        if length in length_count:
            length_count[length] += 1
        else:
            length_count[length] = 1
    return length_count
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_20(task_20))
print(session.get_completion_percentage())
# VERIFICATION PROCESS

