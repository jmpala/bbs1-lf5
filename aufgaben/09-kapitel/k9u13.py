"""
Aufgabe K9 | A13: Schreiben Sie eine Funktion „wechselautomat(geld)“ welcher einen geraden Betrag X
nimmt und in der Lage ist 20€ Scheine und 1€ Münzen auszugeben. Der Automat wird immer möglichst
viele Scheine bzw. möglichst wenig Münzen ausgeben.
Bsp: wechselautomat(55)
“2x 20€ Scheine und 15x 1€ Münzen“
"""


def wechselautomat(geld):
    res = geld // 20
    rest = geld % 20
    print("{}x 20€ Scheine und {}x 1€ Münzen".format(res, rest))


wechselautomat(100)
