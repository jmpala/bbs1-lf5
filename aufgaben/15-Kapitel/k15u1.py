"""
Aufgabe K15 | A1:Erstelle eine Klasse Haus inkl. Konstruktor,
welches über folgende Attribute verfügt: Straße, Hausnummer,
Farbe, Preis, Stockwerksanzahl, Quadratmeter.
"""


class Haus:
    def __init__(self, street, haus_number, color, price, floors, size):
        self.size = size
        self.floors = floors
        self.price = price
        self.color = color
        self.haus_number = haus_number
        self.street = street

    def __str__(self):
        print("street: ", self.street)
        print("haus_number: ", self.haus_number)
        print("color: ", self.color)
        print("price: ", self.price)
        print("floors: ", self.floors)
        print("size: ", self.size)
        return ""


my_haus = Haus(
    "strasse 1",
    "1",
    "green",
    10,
    1,
    40
)

print(my_haus)
