"""
Aufgabe K15 | A4:Füge der Klasse die Methode neuer_anstrich(farbe) hinzu,
die eine neue Farbe nimmt und den Wert entsprechend abändert. Erstelle dann ein Objekt,
dessen Farbe nachträglich geändert wird und gebe diesen Wert auf der Konsole erneut aus.
"""


class Haus:
    def __init__(self, street, haus_number, color, price, floors, size):
        self.size = size
        self.floors = floors
        self.price = price
        self.color = color
        self.haus_number = haus_number
        self.street = street

    def change_color(self, color):
        print("change color from ", self.color, " to ", color)
        self.color = color

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


my_haus.change_color("red")
