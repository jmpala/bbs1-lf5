"""
Aufgabe K13 | A3: Schreibe eine Funktion read_one_value(), welches jeden Wert (z. B.) Markus einzeln
auf der Konsole ausgibt und danach einen Zeilenumbruch erzeugt. Ausgabe ist also:
Markus
Burg
19
Julia
"""


def read_one_value():
    with open('./k13u3.txt', 'r') as file:
        for line in file:
            for word in line.split(','):
                print(word.strip())
            print()


read_one_value()
