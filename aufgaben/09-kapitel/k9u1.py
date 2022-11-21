"""
Aufgabe	K9	|	A1 Implementiere	diese	Aufgabe	rekursiv! (Fibonacci-Folge)
"""


def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)


print(str(fib(11)))
