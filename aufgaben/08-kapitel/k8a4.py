'''
Aufgabe	K8	|	A4: Nach	dem	Auto	würdest	du	dir	gerne	ein	neues	Smartphone	kaufen.	Hier	sind	deine	
Ansprüche	allerdings	etwas	höher.	Der	Preis	sollte	unter	1000€	liegen;	das	Smartphone	sollte	mindestens	3	
Rückkameras	besitzen;	2	Tage	ohne	zu	laden	durchhalten	und	von	der	Marke	Apple	oder	Samsung	sein.	
'''

MAXIMAL_HANDY_PREIS = 999
MINIMUM_KAMERAS = 3
MINIMUM_LADEN = 2 # Tage
MARKE = ["apple", "samsung"]

def kauf_checken(preis, kameras, laden, mark):
    
    if preis > MAXIMAL_HANDY_PREIS or kameras < MINIMUM_KAMERAS or laden < MINIMUM_LADEN:
        return False

    for m in MARKE:
        if m == mark:
            return True

    return False


preis = 999
kameras = 3
laden = 2
mark = "apple"

res = kauf_checken(preis, kameras, laden, mark)
print(res)