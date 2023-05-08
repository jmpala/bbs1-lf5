"""
Aufgabe K16 | A1:Erstellen Sie zur Hausklasse jeweils einen Getter & Setter
für die Attribute Preis und Quadratmeter. Im Setter soll jeweils ausgeschlossen werden,
dass negative Werte eingegeben werden können. Wird ein negativer Wert nachträglich
eingegeben soll eine Warnmeldung in der Konsole erscheinen und der Wert wird nicht hinzugefügt.
Falls der Wert valide ist, wird dieser hinzugefügt.
"""


class Haus:
    def __init__(self, street, haus_number, color, price, floors, size):
        self._size = size
        self.floors = floors
        self._price = price
        self.color = color
        self.haus_number = haus_number
        self.street = street

    def __str__(self):
        print("street: ", self.street)
        print("haus_number: ", self.haus_number)
        print("color: ", self.color)
        print("price: ", self._price)
        print("floors: ", self.floors)
        print("size: ", self._size)
        return ""

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("price must be positive")
            return
        self._price = value

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        if value > 0:
            print("size must be positive")
            return
        self._size = value


my_haus = Haus(
    "strasse 1",
    "1",
    "green",
    10,
    1,
    40
)

my_haus.size = -1
my_haus.price = -1

print(my_haus)
