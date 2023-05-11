"""
Aufgabe K13 | A1: Erstelle eine .txt Datei mit folgendem Inhalt:
Markus,Burg,19
Julia,Scherger,18
Murad,Surgy,18
"""

with open('./k13u1.txt', 'r') as data:
    for line in data:
        print(line.strip())
