"""
Aufgabe K11 | A5: Schreibe eine Funktion foo(number), die eine ganze Zahl nimmt und überprüft ob
diese positiv, negativ, gerade, ungerade oder gar keine Integer ist. Die Ausgabe soll in Form eines
Dictionaries erfolgen.

Beispiel:

foo(10) => {“vorzeichen: positiv“, “parität“: “gerade“}
foo(-5.3) => {“vorzeichen: negativ“, “parität“: “kein Integer“}
"""


def chechNumber(num: int | float):
    res = {}

    if num >= 0:
        res['vorzeichen'] = 'positiv'
    else:
        res['vorzeichen'] = 'negativ'

    if isinstance(num, int):
        res['paritaet'] = 'gerade' if num % 2 == 0 else 'ungerade'
    if isinstance(num, float):
        res['paritaet'] = 'kein Integer'

    return res


print(chechNumber(10))
print(chechNumber(-9))
print(chechNumber(-5.3))
