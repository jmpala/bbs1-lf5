"""
Aufgabe	K9	|	A9: Erweitere	das	Spiel	„crackingNumber“.	Diesmal	wählst	du	eine	Zufallszahl	aus	und	der
Computer	muss	raten.	Überlege	dir	vorher,	mit	welcher	Strategie	der	Computer	vorgehen	soll,	um	mit
möglichst	wenigen	Versuchen	sein	Ziel	zu	erreichen
"""


def guess_number(number, guess):
    if number == guess:
        return 0
    elif number >= guess:
        return 1
    elif number <= guess:
        return -1


def strategy():



min = 0
max = 100
num = int(input("Give a number from 0 to 100..."))

while True:
