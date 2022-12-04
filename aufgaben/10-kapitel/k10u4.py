"""
Aufgabe K10 | A4: Implementieren Sie eine zweite Selectionsort-Funktion. Diesmal soll der Algorithmus
in-place arbeiten.
"""


def selection_sort(liste: list):  # in-place
    for head in range(0, len(liste)):
        i_small = head
        for tail in range(head + 1, len(liste)):
            if liste[i_small] > liste[tail]:
                i_small = tail
        liste[head], liste[i_small] = liste[i_small], liste[head]
    return liste


meine_liste = [6, 2, 8, 3, 2]
print(selection_sort(meine_liste))
