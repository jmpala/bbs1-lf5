"""
Aufgabe		K9	|	A11: Programmiere	eine	Kinositzverteilung.	Der	Kinosaal	besteht	aus	6	Reihen	mit	je	9
Sitzplätzen.	Die	Loge	besitzt	2	Reihen	mit	je	9	Plätzen.	Dein	Programm	soll	zufallsgeneriert	einige	Sitze
als	belegt	hinterlegen	und	den	gesamten	Sitzplan	via	Konsole	optisch	ansprechend	ausdrucken.
"""
import random


def print_sits(arr):
    for sit in arr:
        print("".join(sit))


def random_sit_state():
    num = random.randint(0, 1)
    return "🟢" if num == 0 else "🟠"


sits = 9
cinema_rows = 6
loge_rows = 2

cinema_sits = [["" for x in range(sits)] for y in range(cinema_rows + loge_rows)]

for x, row in enumerate(cinema_sits):
    for y, seat in enumerate(row):
        v = random_sit_state()
        cinema_sits[x][y] = v

print("Cinema sits...")
print_sits(cinema_sits)
