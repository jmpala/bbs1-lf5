"""
Aufgabe K14 | A2: Wie kann verhindert werden, dass ein erneuter Aufruf der Funktion dazu führt, dass
der ursprüngliche Inhalt überschrieben wird? Beschreibe dein Vorgehen in einer .py Datei und
implementiere die Lösung
"""


def generate_numbers() -> list:
    aux = []
    for num in range(1, 11):
        aux.append(str(num))
    return aux


def write_numbers() -> None:
    with open('./my_first_numbers_append.csv', 'a') as file:
        file.write(
            ','.join(generate_numbers()) + '\n'
            )


write_numbers()
