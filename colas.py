#/usr/bin/env python

############################################
############################################
## Autor:   Daniel Romo Garcia            ##
## Email:   danielromogarcia@gmail.com    ##
## Blog:    d4nnr.blogspot.com            ##
## Twitter: @d4nnr                        ##
############################################
############################################

#Creamos una lista vacia
cola = []

#Creamos un Menu con 4 opciones
def main():
        print("1 Insertar cola")
        print("2 Borrar en cola")
        print("3 Listar cola")
        print("4 Salir")
        
        option = input("Elija una opcion: ")

        #Esta opcion permite encolar el numero en la lista
        if str(option)=="1":
                elemento = input(" Introduzca el numero a encolar: ")
                cola.append(elemento)
                print(" numero encolado con exito ")
                main()

        #Esta opcion saca de la lista el numero en orden de ingreso
        elif str(option)=="2":
                if len(cola)>0:
                   print("El numero: ",cola.pop(0),"fue desencolado")
                   main()
                else:
                   print("Cola vacia")
                   main()

        #Esta opcion imprime en pantalla la cola
        elif str(option)=="3":
                for i in cola:
                   print("cola: ",i)
                main()

        #Esta opcion permite salir de la ejecucion del codigo
        elif str(option)=="4":
                exit()
        else:
                print("Seleccione una opcion valida.")
                main()

main()
