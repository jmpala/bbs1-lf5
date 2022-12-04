"""
Aufgabe K10 | A9: Gegeben ist folgende Funktion:
def blablub(lis,obj):
Vervollständige die Funktion so, dass diese überprüft ob das Objekt bereits Teil der Liste ist. Falls nicht,
wird das Objekt an die Liste angehangen und die Liste zurückgegeben.
"""


def blablub(lis: list, obj):
    if not lis.count(obj) > 0:
        lis.append(obj)
    return lis


print(blablub([1, 2], 3))
print(blablub([1, 2, 3], 3))
