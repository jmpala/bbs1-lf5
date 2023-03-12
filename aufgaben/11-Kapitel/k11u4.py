"""
Aufgabe K11 | A4: Schreibe ein Programm, in dem ein Benutzer beliebig lange Länder inkl. Hauptstädte
eingeben kann, bis er Beenden eintippt.

Die Länder + Hauptstädte werden in einem Dictionary gespeichert und danach auf der Konsole
ausgegeben. Das Ausgabeformat lautet:

“ Land | Hauptstadt“
“1. Deutschland | Berlin “
“2. Frankreich | Paris “
"""


states_capitals_dic = {}

print("Please enter the states and its corresponding capital")

while True:
    state = input("Enter State or \"END\" to end execution")

    if state.lower() == "end":
        break

    capital = input("Enter the capital city of " + state)

    states_capitals_dic[state] = capital

if len(states_capitals_dic) < 1:
    exit("No states entered!!!")

print("The inputted values are: ")
print(states_capitals_dic)
