"""
Aufgabe K10 | A5: Implementieren Sie den Bubblesortalgorithmus (in-place)
"""


def bubble_sort(liste: list):  # in-place
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(0, len(liste) - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                is_swapped = True
    return liste


meine_liste = [6, 2, 8, 3, 2]
print(bubble_sort(meine_liste))
