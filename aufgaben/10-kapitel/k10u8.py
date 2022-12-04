"""
Aufgabe K10 | A8: Folgende Liste ist gegeben passwords = [“ababa“, „baab“,“sdiopc“,“ajkwei“,“bab“]
Erstelle eine Funktion, die die Liste nimmt und überprüft ob „ab“ oder „ba“ in den jeweiligen Strings
vorkommt. Wenn ja, soll das Passwort komplett ausgedruckt werden.
"""


passwords = ["ababa", "baab", "sdiopc", "ajkwei", "bab"]

match = ["ab", "ba"]


for password in passwords:
    count = 0
    count += password.count("ab")
    count += password.count("ba")
    if count > 0:
        print(password)
