"""
ufgabe	K9	|	A3: Schreibe	eine	Funktion	„countdown“,	die	von	10	bis	zur	0	herunterzählt	und	die
einzelnen	Zahlen	ausgibt.
"""


def countdown(num):
    print(num)
    if num == 0:
        return
    return countdown(num - 1)


countdown(10)
