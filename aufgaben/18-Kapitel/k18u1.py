""""
Aufgabe	K18	|	A1: Erstelle	für	unser	„RPG-Fighting-Game“	eine	Vaterklasse	„Creature“,	sowie	die
Kindklassen „Mage“	und	“Warrior“.	Die	Vaterklasse	beinhaltet	neben	den	Attributen	„hp,name,size,gold“,
die	Methoden	„roll_dice(int)“	und	„fist_hit()“.	Beide	Methoden	sollen	abstrakt	sein	und	in	den
Kindklassen entsprechend	implementiert	werden.	Bei	roll_dice(int)	wird	imaginär	gewürfelt.	Der
Parameter	entspricht	den	Seiten	des	Würfels.	Also	z.	B.	roll_dice(6)	->	1	bis	6	als	möglicher	Output.
fist_hit()	verwendet	roll_dice um	den	Schaden	zu	ermitteln.	Der	Magier	macht	1d3	Schaden,	der	Krieger
hingegen	1d4.	Daher	sollten	sich	die	Implementierungen	entsprechend	unterscheiden
"""

from Mage import Mage
from Warrior import Warrior


mage = Mage(10, "Gandalf", 1, 100)
warrior = Warrior(10, "Conan", 1, 100)

mage.hit_first()
warrior.hit_first()
