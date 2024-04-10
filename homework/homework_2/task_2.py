# Aceasta este a doua ta sarcină legată a leciei legate de stringuri în python

# Creează o variabilă numită `name` și seteaz-o la numele tău
name = "Adriano!"

# Acum afișează valoarea variabilei `name` folosind funcția `print`
print(f"name = {name}")

# Acum creează o nouă variabilă numită `name2` și seteaz-o la valoarea variabilei `name` și afișează valoarea variabilei `name2` folosind funcția `print`
name2 = name
print(f"name2 = {name2}")

# Acum printează ultimul caracter al variabilei `name` folosind indexarea
print(f"last char {name[-1]}")

# Acum printează primele 3 caractere ale variabilei `name` folosind slicing
print(f"first 3 chars {name[:3]}")

# Acum printează valoarea variabilei `name` în majuscule folosind metoda `upper`
print(f"upper {name.upper()}")

# Acum printează valoarea variabilei `name` în minuscule folosind metoda `lower`
print(f"lower {name.lower()}")

# Acum printează concatenarea variabilelor `name` și `name2`
print(f"concat {name + name2}")

# Creează o variabilă `text` și setează-i un text la alegere, cu restricția ca acesta să conțină mai multe rânduri
text = """
salut
python
adrian
bootcamp
"""

# Verifică dacă variabila `text` conține cuvântul `python`
print(text.__contains__("python"))

# Folosește metoda replace pentru a înlocui litera `a` din variabila `text` cu litera `e`
print(text.replace("a", "e"))

# Folosește metoda split pentru a transforma variabila `text` într-o listă de cuvinte
print(text.split())

# Creează un f-string care să conțină variabilele `name` și `name2`
f_string = f"{name} + {name2}"

# Verifică dacă string-ul creat se termină cu `!`
print(f"check end = {f_string.endswith('!')}")

# Verifică dacă string-ul creat începe cu `Hello`
print(f"start with = {f_string.startswith('Hello')}")

# Identifică indexul unde se află `!` în string-ul creat
print(f"find index of '!' = {f_string.find('!')}")

# Identifică indexul unde se află `o` în string-ul creat folosind altă metodă
print(f"find index of 'o' = {f_string.index('o')}")

# Utilizând format string-uri, creează un string care să conțină variabilele `name` și `name2`
f_string_2 = f"name = {name}, name2 = {name2}"

# Concatenează string-ul creat cu string-ul `text`
f_string_concat = text + f_string_2

# Afișează lungimea string-ului creat
print(f_string_concat)
print(len(f_string_concat))

# Aceasta a fost tot pentru această sarcină

