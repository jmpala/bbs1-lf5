"""
Aufgabe K10 | A2: Schreibe eine Funktion meinSort(meineListe), die deine unsortierte Liste nimmt, diese
nach deiner Strategie sortiert und ausgibt.
"""


def sort(liste: list):
    for head in range(0, len(liste)):
        for tail in range(head + 1, len(liste)):
            if liste[head] > liste[tail]:
                liste[head], liste[tail] = liste[tail], liste[head]


liste = [6, 2, 8, 3, 2]
sort(liste)
print(liste)
