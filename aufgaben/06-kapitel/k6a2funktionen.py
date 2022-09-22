'''
Ausgabe 3:

    Ich vermute das, die Variablen, die nicht gennant sind und auch diese Rechnen beinflußen könnten sind:
        - die Hitze
        - der Zustand des Autos
        - die unreguler Geschwindigkeit durch dem Strecke

'''
def spritkosten(km, spritverbrauch, literkosten):
    return ((spritverbrauch / km) * 100) * literkosten;

'''
Ausgabe 4:

    Die untere Zeile ist wichtig, wiel ohne die, wird der Interpretar sie ausgeführt, wenn
    woanders diese Datei aufgeruft wird.

'''
if __name__ == "__main__":
    print(spritkosten(1, 10, 2))