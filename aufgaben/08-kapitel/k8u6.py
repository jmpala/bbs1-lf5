'''
Aufgabe	K8	|	A6: Erstelle	einen	Switch-Case	Block,	der	als	case entweder	den	String	„Stein“,	„Schere“	oder	
„Papier“	nimmt	und	entsprechend	auf	der	Konsole	ausgibt,	welcher	Inhalt	in	der	Variable	vorher	eingetragen	
wurde.	Als	default-Fall	soll	„Weder	noch	…“	ausgegeben	werden!
'''

def switch(case):
    cases = {
        "stein" : "stein",
        "schere" : "schere",
        "papier" : "papier",
    }
    print(cases.get(case, "Weder noch …"))

switch("stein")
switch("schere")
switch("papier")
switch("")