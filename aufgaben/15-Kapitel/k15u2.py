"""
Aufgabe K15 | A2:Erstelle ein Objekt der Klasse Haus mit beliebigen Werten.
Gebe danach alle Werte auf der Konsole wieder aus.
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
