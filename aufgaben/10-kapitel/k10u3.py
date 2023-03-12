"""
Aufgabe K10 | A3: Implementieren Sie den Selectionsortalgorithmus als Funktion. Dieser soll out-ofplace
(also mit 2 Listen) arbeiten
"""


def selection_sort(liste: list):  # out-of place
    ordered_liste = []
    while len(liste) > 0:
        i_small = 0

        for i in range(1, len(liste)):
            if liste[i_small] > liste[i]:
                i_small = i

        ordered_liste.append(liste.pop(i_small))

    return ordered_liste


meine_liste = [6, 2, 8, 3, 2]
print(selection_sort(meine_liste))
