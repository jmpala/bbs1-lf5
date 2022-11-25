"""
Aufgabe K9 | A14: Erweitern Sie das Programm dahingehend, dass der Automat nun auch 50€ Scheine,
10€ Scheine, 5€ Scheine und 2€ Münzen unterstützt. Schreiben Sie hier 2 Varianten:
In Variante 1 versucht der Automat möglichst wenig Scheine und Münzen auszugeben
In Variante 2 versucht der Automat die Scheine und Münzen gleichmäßig auszugeben, damit nicht der
Fall eintritt, dass eine Scheinart bzw. Münzart frühzeitig erschöpft ist.

Variante 2
"""


def wechselautomat(geld):
    res = geld // 20
    rest = geld % 20
    print("{}x 20€ Scheine und {}x 1€ Münzen".format(res, rest))


wechselautomat(100)
