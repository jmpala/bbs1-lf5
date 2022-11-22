"""
Aufgabe	K9	|	A9: Erweitere	das	Spiel	„crackingNumber“.	Diesmal	wählst	du	eine	Zufallszahl	aus	und	der
Computer	muss	raten.	Überlege	dir	vorher,	mit	welcher	Strategie	der	Computer	vorgehen	soll,	um	mit
möglichst	wenigen	Versuchen	sein	Ziel	zu	erreichen
"""
import random


def guess_number(number, guess):
    if number == guess:
        return 0
    elif number >= guess:
        return -1
    elif number <= guess:
        return 1


def game_loop(number, min_guess, max_guess, turns=100):
    head = min_guess
    tail = max_guess
    guess = random.randint(head, tail)
    while turns > 0:
        res = guess_number(number, guess)
        match res:
            case 1:
                tail = guess
            case -1:
                head = guess
            case 0:
                print("Computer guessed the value...")
                print("Value was: " + str(guess))
                print("Remaining turns: " + str(turns))
                exit(0)
            case _:
                print("Not supported value")
                exit(-1)
        turns -= 1
        guess = random.randint(head, tail)


begin = 0
end = 100
turns = 20
num = int(input("Give a number from {} to {}...".format(begin, end)))
game_loop(num, begin, end, turns)
print("Computer did not guessed the number...")


