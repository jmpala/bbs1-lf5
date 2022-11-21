"""
Aufgabe	K9	|	A6: Erweitere	deine	Funktion	„countingStars“	dahingehend,	dass	die	Anzahl	der	Sterne
wieder	abnimmt.	Beispiel	Zahl	=	3;
*
**
***
**
*
"""

def printStars(num):
    if num > 0:
        print("*", end="")
        printStars(num - 1)
    else:
        return


def incrementPrint(num, i=1):
    if i <= num:
        printStars(i)
        print()
        incrementPrint(num, i + 1)


def decrementPrint(num):
    if num > 0:
        printStars(num)
        print()
        decrementPrint(num - 1)


def countingStars(num):
    incrementPrint(num - 1)
    decrementPrint(num)


countingStars(5)
