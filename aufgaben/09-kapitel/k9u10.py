"""
Aufgabe K9 | A10:Erstelle ein Programm „QuestionAnswer.py“. Dieses Programm stellt dem Benutzer mindestens 3 Fragen.
Für jede richtige Antwort soll der Spieler einen Punkt bekommen. Am Ende erscheint die Gesamtpunktzahl.
"""

questions = [
    "Who created Linux GNU?\n1. Linus Torvalds\n2. Richard Stallman\n3. Both",
    "What is GNU?\n1. Is the complete name of Linux\n2. Is a collection of programms added to the first Linux "
    "distribution\n3. Is an OS",
    "Who created the Free Software Foundation?\n1. Linus Torvalds\n2. Richard Stallman\n3. Both"
]

answers = [3, 2, 2]
points = 0

print("Answer the following questions...")
for i, q in enumerate(questions):
    print("{}) {}".format(i, q))
    res = int(input("Enter the answer..."))
    if answers[i] == res:
        points += 1

print("You have {} points...".format(points))
