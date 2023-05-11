"""
Aufgabe K13 | A2: Schreibe eine Funktion read_every_line(), die beim Aufruf jede Zeile auf der Konsole
ausgibt.
"""


def read_every_line():
    with open('./k13u2.txt', 'r') as file:
        for line in file:
            print(line.strip())


read_every_line()
