"""
Aufgabe K10 | A11:
Schreibe eine Funktion, die eine Liste als Parameter nimmt. Entweder wird das letzte Element der Liste
zurückgeliefert oder (falls die Liste leer sein sollte), wird der String „Leere Liste“ zurückgeliefert
"""


def last_or_message(liste: list):
    if len(liste) > 0:
        return liste[len(liste) - 1]
    else:
        return "List is empty..."


print(last_or_message([1, 2, 3]))
