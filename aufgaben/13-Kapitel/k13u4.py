"""
Aufgabe K13 | A4: Schreibe eine Funktion just_eighteen(), welches nur Personen auf die Konsole druckt,
die genau 18 Jahre alt sind.
"""


def just_eighteen():
    with open('./k13u4.txt', 'r') as file:
        for line in file:
            if int(line.split(',')[2].strip()) >= 18:
                print(line.strip())


just_eighteen()
