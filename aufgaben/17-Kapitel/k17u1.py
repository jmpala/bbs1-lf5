"""
Aufgabe	K17 | A1: Erstelle	eine	Vaterklasse	Fahrzeug	und	die	Kindklassen Motorrad	und	Auto. Erstelle
eine	entsprechende	Vererbungshierarchie	zwischen	den	Klassen
"""


class Vehicle:
    def __init__(self, model, speed, color):
        self.model = model
        self.speed = speed
        self.color = color

    def __str__(self):
        return 'Model ' + str(self.model) \
            + '\nSpeed ' + str(self.speed) \
            + '\nColor ' + str(self.color)


class Car(Vehicle):
    def __init__(self, model, speed, color, seats):
        super().__init__(model, speed, color)
        self.seats = seats

    def __str__(self):
        return super().__str__() \
            + '\nSeats ' + str(self.seats)


class Motorbike(Vehicle):
    def __init__(self, model, speed, color, sidecar):
        super().__init__(model, speed, color)
        self.sidecar = sidecar

    def __str__(self):
        return super().__str__() \
            + '\nSidecar ' + str(self.sidecar)


car_1 = Car(
    'BMW S3',
    240,
    'FFFFFF',
    4
)

moto_1 = Motorbike(
    'Kawasaki Ninja',
    300,
    'FF0000',
    False
)

print(car_1)

print(moto_1)