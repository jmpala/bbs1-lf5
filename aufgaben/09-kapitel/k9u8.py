"""
Aufgabe	K9	|	A8: Schreibe	eine	Funktion	„cancel“,	die	solange	Eingaben	vom	Benutzer	annimmt,	bis
dieser	das	Wort	„Beenden“	eintippt.	Das	Programm	wird	dann	entsprechend	beendet!
"""


def cancel():
    inp = str(input("Enter input: ")).lower()
    if inp == "beenden":
        print("Terminating programm")
        return
    cancel()


cancel()
