"""
Aufgabe K15 | A5:Erstelle eine neue Hausliste mit 3 Hausobjekten.
Danach soll überprüft werden, ob ein Haus über 200.000€ kostet. Falls ja, wird das Haus aus der
Liste entfernt. Gebe anschließend die Liste auf der Konsole aus.
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
    10000,
    1,
    40
)

my_haus_2 = Haus(
    "strasse 2",
    "2",
    "green",
    20000,
    1,
    40
)

my_haus_3 = Haus(
    "strasse 3",
    "3",
    "green",
    19999,
    1,
    40
)

my_haus_list = [my_haus, my_haus_2, my_haus_3]

for haus in my_haus_list:
    if haus.price >= 20000:
        my_haus_list.remove(haus)

for haus in my_haus_list:
    print(haus)
