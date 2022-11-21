"""
Aufgabe		K9	|	A7: Erstelle	ein	Mini-Spiel	mit	dem	Namen	„CrackingNumber“.	Das	Programm	erzeugt
eine	zufällige	Zahl	zwischen	0	und	100	(Google:	„Python	Zufallszahl	(Random)“	für	Hilfe)	und	gibt	dem
Benutzer	5	Eingabeversuche.	Bei	jeder	Eingabe	erhält	der	Benutzer	den	Hinweis,	ob	die	erzeugte	Zahl
größer	oder	kleiner	ist.	Sollte	der	Benutzer	innerhalb	von	5	Eingaben	die	richtige	Zahl	erraten	erscheint
eine	Sieger-Nachricht.	Ansonsten	wird	das	Programm	mit	einer	entsprechenden	Nachricht	terminiert!
"""
import random


def gameloop(turn=5, num=0, guess=0):
    guess = int(input("Enter a guess..."))
    if guess > num:
        print("Guess is bigger than the number")
    elif guess < num:
        print("Guess is smaller than the number")
    else:
        print("You guessed the number!")
        exit()
    if turn - 1 < 1:
        print("No more tries")
        print("Terminating the programm")
        exit()
    gameloop(turn - 1, num, guess)


print("Guess the number between 0 and 100...")
num = random.randint(0, 100)
print(num)
gameloop(num=num)
