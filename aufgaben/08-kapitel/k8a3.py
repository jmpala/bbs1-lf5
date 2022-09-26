'''
Aufgabe	K8	|	A3: Du	möchtest	dir	ein	neues	Auto	kaufen.	Als	Bedingung	ist	dir	wichtig,	dass	das	Auto	
unter	20.000€	kostet	und	eine	Klimaanlage	besitzt.	Schreibe	ein	Programm,	welches	diese	beiden	
Bedingungen	abprüft	und	entweder	„Auto	wird	gekauft“	oder	„Auto	wird	wegen	XY	nicht	gekauft“	ausgibt.
'''

MAXIMAL_AUTO_KOSTEN = 20000

def kauf_checken(kost, has_klima):
    kann_kaufen = True
    grund_liste  = []

    if kost > MAXIMAL_AUTO_KOSTEN:
        grund_liste.append("zu teuer")
        kann_kaufen = False
    if not has_klima:
        grund_liste.append("keine Klimaanlage")
        kann_kaufen = False

    if kann_kaufen:
        print("Auto wird gekauft")
        return

    print("Auto wird wegen")
    for grund in grund_liste:
        print(grund)
    print("nicht gekauft")

    


auto_kosten = 20001
has_klimaanlage = False

kauf_checken(auto_kosten, has_klimaanlage)



