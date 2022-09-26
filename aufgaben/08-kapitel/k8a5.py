'''
Aufgabe	K8	|	A5:	Wenn	es	regnet	und	du	mindestens	20€	übrig	hast	oder	dein/e	Freund/in	zahlt,	geht	ihr	
ins	Kino.	Ansonsten	bleibt	ihr	zuhause	…	
Erstelle	hierzu	ebenfalls	ein	Programm	mit	entsprechender	Ausgabe
'''

from operator import truediv


MINDESTEN_GELD = 20

def gehe_im_kino(regnet, geld, bezahlt):
    if regnet and (geld >= MINDESTEN_GELD or bezahlt):
        return True
    return False

es_regnet = True
geld = 20
freund_bezahlt = True

res = gehe_im_kino(es_regnet, geld, freund_bezahlt)
print(res)