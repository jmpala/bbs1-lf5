"""
Aufgabe K14 | A3: Schreibe eine Funktion „super_fun(number)“, welche eine Zahl nimmt und die Anzahl
an Dateien nach dem Schema „file1.txt“, „file2.txt“ usw. erstellt.
"""

import os
from pathlib import Path


def super_fun(number):
    try:
        os.mkdir('./test')
    except FileExistsError:
        pass
    for i in range(1, number + 1):
        with open('./test/file' + str(i) + '.txt', 'w') as file:
            pass


super_fun(9999)
