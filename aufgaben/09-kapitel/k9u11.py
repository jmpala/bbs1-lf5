"""
Aufgabe		K9	|	A11: Programmiere	eine	Kinositzverteilung.	Der	Kinosaal	besteht	aus	6	Reihen	mit	je	9
Sitzplätzen.	Die	Loge	besitzt	2	Reihen	mit	je	9	Plätzen.	Dein	Programm	soll	zufallsgeneriert	einige	Sitze
als	belegt	hinterlegen	und	den	gesamten	Sitzplan	via	Konsole	optisch	ansprechend	ausdrucken.
"""


def print_sits(arr):
    for sit in arr:
        print("".join(sit))


sits = 9
cinema_rows = 6
loge_rows = 2

cinema_sits = [["🟢"] * sits ] * (cinema_rows + loge_rows)

booked = {}

print("Cinema sits...")
print_sits(cinema_sits)
