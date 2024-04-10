# Aceasta este a doua sarcină legată de booleeni în python
# Creați o variabilă numită `is_student` și setați-o la `True`
is_student = False
# Acum tipăriți valoarea variabilei `is_student` folosind funcția `print`
print(f"{is_student}")
# Acum creați o nouă variabilă numită `is_child` și setați-o la `False` și tipăriți valoarea variabilei `is_child` folosind funcția `print`
is_child = True
print(f"{is_child}")
# Acum utilizați operatorul `and` pentru a verifica dacă atât `is_student`, cât și `is_child` sunt `True` și tipăriți rezultatul folosind funcția `print`
if is_student and is_child:
    print("Both are true")
# Acum utilizați operatorul `or` pentru a verifica dacă cel puțin una dintre `is_student` și `is_child` este `True` și tipăriți rezultatul folosind funcția `print`
if is_student or is_child:
    print("At least one is true")
# Acum utilizați operatorul `not` pentru a verifica dacă `is_student` este `False` și tipăriți rezultatul folosind funcția `print`
if not is_student:
    print("Not a student")