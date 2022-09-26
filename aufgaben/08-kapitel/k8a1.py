'''
Aufgabe	K8	|	A1: Erstelle	ein	Programm	welches	zwei	Integer	nimmt	und	überprüft	welche	der	beiden	
Zahlen	größer	ist.	Diese	soll	im	Terminal	ausgegeben	werden!
'''

def return_bigger_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

print(type(num1))
print(type(num2))

print("The bigger number is: ", return_bigger_number(num1, num2))

