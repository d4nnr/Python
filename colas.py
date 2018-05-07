#/usr/bin/env python

cola = []

def main():
        print("1 Insertar cola")
        print("2 Borrar en cola")
        print("3 Listar cola")
        print("4 Salir")
        option = input("Elija una opcion: ")

        if str(option)=="1":
                elemento = input(" Introduzca el numero a encolar: ")
                cola.append(elemento)
                print(" numero encolado con exito ")
                main()

        elif str(option)=="2":
                if len(cola)>0:
                   print("El numero: ",cola.pop(0),"fue desencolado")
                   main()
                else:
                   print("Cola vacia")
                   main()

        elif str(option)=="3":
                for i in cola:
                   print("cola: ",i)
                main()

        elif str(option)=="4":
                exit()
        else:
                print("Seleccione una opcion valida.")
                main()

main()
