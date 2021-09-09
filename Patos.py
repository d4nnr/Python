# @D4nnR
# Tradicional videojuego llevado a las noches etílicas de la juventud. 
# Un cazador de patos y su fiel perro de caza están agazapados a la espera de un objetivo. 
# Al ver determinada cantidad de patos el perro le indica al cazador la cantidad de patos que ve, 
# y la cantidad de patas totales. Luego el cazador dispara 1 bala a cada uno y se escuchan caer al agua los objetivos.

from sys import argv
import math

try:
    n = int(input("""Ingresa la cantidad de patos a atrapar: """))                                       
    n2 = n*2
    print("Elegiste", n, "Patos")
    print("Tienen", n2, "Patas")

    for i in range(n):
        print ("Pum!")
    for i in range(n):
        print ("Splash!")

except ValueError:
    print ('Entra un valor válido')
