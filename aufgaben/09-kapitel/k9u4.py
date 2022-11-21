"""
Aufgabe	K9	|	A4: Schreibe	eine	Funktion	„ende“,	die	solange	Zahlen	vom	Benutzer	einliest,	bis	dieser	eine
0	eingibt.	Dann	soll	das	Programm	mit	einer	entsprechenden	Nachricht	beendet	werden
"""


def ende():
    inp = int(input("Insert number: "))
    if inp == 0:
        return
    ende()


ende()
print("Exiting program")
