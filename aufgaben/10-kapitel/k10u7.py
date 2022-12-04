"""
Aufgabe K10 | A7: Versuche den Quicksortalgorithmus in Python umzusetzen. Schreibe hierzu eine
entsprechende Funktion, welches eine Liste nimmt und diese mit Quicksort sortiert.
"""

import math


def quick_sort(liste: list):
    pivot_index = math.floor(len(liste)/2)
    pivot = liste.pop(pivot_index)
    lower = []
    bigger = []
    test = []

    if len(liste) > 0:
        for n in liste:
            if n <= pivot:
                lower.append(n)
            else:
                bigger.append(n)

    if len(lower) > 0:
        test.extend(quick_sort(lower))
    test.append(pivot)
    if len(bigger) > 0:
        test.extend(quick_sort(bigger))

    return test


meine_liste = [6, 3, 8, 2, 3, 14]
print(quick_sort(meine_liste))
