"""
Aufgabe K15 | A3:Erstelle 3 verschiedene Hausobjekte und speichere diese in einer Liste.
Lösche danach das letzte Haus in der Liste und gebe die Liste entsprechend auf der Konsole aus.
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

my_haus2 = Haus(
    "strasse 2",
    "2",
    "red",
    20,
    2,
    80
)

my_haus3 = Haus(
    "strasse 3",
    "3",
    "blue",
    30,
    3,
    120
)

my_haus_list = [my_haus, my_haus2, my_haus3]

my_haus_list.pop()

for haus in my_haus_list:
    print(haus)
