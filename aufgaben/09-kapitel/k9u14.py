"""
Aufgabe K9 | A14: Erweitern Sie das Programm dahingehend, dass der Automat nun auch 50€ Scheine,
10€ Scheine, 5€ Scheine und 2€ Münzen unterstützt. Schreiben Sie hier 2 Varianten:
In Variante 1 versucht der Automat möglichst wenig Scheine und Münzen auszugeben
In Variante 2 versucht der Automat die Scheine und Münzen gleichmäßig auszugeben, damit nicht der
Fall eintritt, dass eine Scheinart bzw. Münzart frühzeitig erschöpft ist.

Variante 1
"""


def print_result(res):
    if len(res) <= 0:
        print("Cant print empty array...")
        return
    for r in res:


# 50, 20, 10, 5, 2, 1
def wechselautomat(geld):
    scheine = [50, 20, 10, 5, 2, 1]
    result = []
    for s in scheine:
        quot = geld // s
        rest = geld % s
        if rest == 0:
            return result
            break
        result.append([s, quot, rest])
    return result






wechselautomat(100)
