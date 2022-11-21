"""
Kapitel	K9	|	A5:	Schreibe	eine	Funktion	„countingStars“,	welches	eine	Zahl	nimmt	und	Sterne	nach
folgendem	Muster	ausgibt.
Zahl	=	2	entspricht:
*
**
Zahl	=	3	entspricht:
*
**
***
usw.
"""

def printStars(num):
    if num > 0:
        print("*", end="")
        printStars(num - 1)
    else:
        return


def countingStars(num, i=1):
    if i <= num:
        printStars(i)
        print()
        countingStars(num, i + 1)


countingStars(5)
