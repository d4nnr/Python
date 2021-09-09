# @D4nnR
# Tradicional videojuego llevado a las noches etílicas de la juventud. 
# Un cazador de patos y su fiel perro de caza están agazapados a la espera de un objetivo. 
# Al ver determinada cantidad de patos el perro le indica al cazador la cantidad de patos que ve, 
# y la cantidad de patas totales. Luego el cazador dispara 1 bala a cada uno y se escuchan caer al agua los objetivos.
# @D4nnR
from sys import argv
import math
try:
    q = int(input("""Quieres cazar o jugar con los patos?: 
    1. Jugar
    2. Cazar
    """))
    n = int(input("""Ingresa la cantidad de patos: """))  
    if n > 0:
        if q == 1:
                if n==1:
                    print("Elegiste", n, "Pato")
                    print("Tienen", n*2, "Patas")
                    for i in range(n):
                        print (i+1, "En la mira!")
                    for i in range(n):    
                        print (i+1, "Atrapado!")
                else:
                    print("Elegiste", n, "Patos")
                    print("Tienen", n*2, "Patas")
                    for i in range(n):
                        print (i+1, "En la mira!")
                    for i in range(n):    
                        print (i+1, "Atrapados!")
        elif q == 2:
                if n==1:
                    print("Elegiste", n, "Pato")
                    print("Tienen", n*2, "Patas")
                    for i in range(n):
                        print (i+1, "Pum!")
                    for i in range(n):    
                        print (i+1, "Splash!")
                else:
                    print("Elegiste", n, "Patos")
                    print("Tienen", n*2, "Patas")
                    for i in range(n):
                        print (i+1, "Pum!")
                    for i in range(n):    
                        print (i+1, "Splash!")
    else:
        print("antimateria (-pato) es difícil de conseguir todavía")
except ValueError:
    print ('Entra un valor válido')
