"""
Aufgabe K10 | A12: Du möchtest für ein Schachturnier jeden Spieler gegen jeden anderen antreten lassen.
Hierfür müssen alle möglichen Kombinationen berücksichtigt werden.
Schreibe eine funktion „all_combinations(playernumber)“, welche die Anzahl der Spieler übergeben
bekommt und jede valide Kombination ausgibt. Z. B.
all_combinations(3) würde zu der Ausgabe
Player 1 vs 2
Player 1 vs 3
Player 2 vs 3
führen. Die Kombinationen 2 vs 1 und 3 vs 1 sind hier nicht zulässige Doppelungen!
"""


def all_combinations(player_number):
    players = []
    for n in range(1, player_number + 1):
        players.append(n)

    for h_num in range(0, len(players) - 1):
        for t_num in range(h_num + 1, len(players)):
            print("{} vs {}".format(players[h_num], players[t_num]))


all_combinations(10)
