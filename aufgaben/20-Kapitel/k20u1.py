""""
Aufgabe	K20	|	A1: Öffne	eine	.txt Datei	auf	deiner	Festplatte	mit	der	open()	Anweisung	(ohne	das
Schlüsselwort	which).
Welche	Fehlermeldungen	können	auftreten?	Erstelle	für	jede	Fehlervariante	eine	entsprechende
Exception,	bei	der	du	den	User	mit	einer	print-Ausgabe	auf	den	Fehler	aufmerksam	machst	und	dort
beschreibst,	was	er	tun	soll	um	den	Fehler	zu	beheben
"""

try:
    file = open("test.txt", "r")
except FileExistsError:
    print("File already exists")
except OSError or IOError:
    print("File can not be opened")
except ValueError:
    print("Encoding Error")
except Exception:
    print("Unknown Error")
    exit(-1)
else:
    print("Do something with the file")
    file.close()
finally:
    print("Ending Programm")

exit(0)
