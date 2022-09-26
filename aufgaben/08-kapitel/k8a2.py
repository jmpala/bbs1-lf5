'''
Aufgabe	K8	|	A2: Das	nachfolgende	Programm	soll	drei	Zahlen	beinhalten,	die	in	aufsteigender	
Reihenfolge	im	Terminal	ausgegeben	werden!
'''

def bubble_sort(list):
    for x in range(0, len(list), 1):
        for y in range(x, len(list), 1):
            if list[x] > list[y]:
                aux = list[x]
                list[x] = list[y]
                list[y] = aux


num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))

num_list = [num1, num2, num3]

bubble_sort(num_list)

print(num_list)

