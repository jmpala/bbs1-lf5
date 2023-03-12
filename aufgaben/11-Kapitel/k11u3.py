"""
Aufgabe K11 | A3: Schreibe eine Funktion supersearch(d,value), welches ein Dictionary und einen value
(Wert) nimmt und diesen Wert im Dictionary sucht. Falls der Wert gefunden wird, soll die Funktion True
zurückliefern, falls nicht False.

Hinweis: build-in Suchfunktionen (z. B. d.get() sind nicht erlaubt!)
"""


def supersearch(d: dict,value: str) -> bool:
    for key in d:
        if key == value:
            return True
    return False


dict = {
    'zerg': 'rush',
    'terran': 'turtle',
    'protos': 'shields'
}

print(supersearch(dict, 'elves'))
print(supersearch(dict, 'terran'))
