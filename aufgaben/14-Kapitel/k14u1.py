"""
Aufgabe K14 | A1: Schreibe eine Funktion, welches die Zahlen von 1 bis 10 erzeugt und diese Zahlen mit
Komma getrennt in eine neue Datei schreibt. Der Dateiname ist „my_first_numbers.csv“.
"""


def generate_numbers() -> list:
    aux = []
    for num in range(1, 11):
        aux.append(str(num))
    return aux


def write_numbers() -> None:
    with open('./my_first_numbers.csv', 'w') as file:
        file.write(
            ','.join(generate_numbers()) + '\n'
            )


write_numbers()
