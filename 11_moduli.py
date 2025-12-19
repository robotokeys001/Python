#Import di tutta la libreria
import math

#Import selettivo 
#Importo solo le funzioni che mi servono
from math import pi, sin, floor, ceil

#Utilizzo la funzione dalla libreria
print(math.sqrt(16))

#Utilizzo solo la funzione che ho importato. Senza math.sqrt()
print(f"Seno in radiali, {sin(90)}")
print(pi)
print(floor(3.9))
print(ceil(3.9))

print(f"Seno in gradi, {math.degrees(math.sin(90))}")