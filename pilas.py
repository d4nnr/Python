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
stack = []

#Creamos un Menu con 4 opciones
def main():
        print("1 Aplilar elemento (entero)")
        print("2 Desapilar elemento")
        print("3 Mostrar pila")
        print("4 Salir")
        option = input("Elija una opcion: ")

        #Esta opcion permite apilar el numero en la lista
        if str(option)=="1":
                elemento = input(" Introduzca el numero a apilar: ")
                stack.append(elemento)
                print(" Elemento apilado ")
                main()

        #Esta opcion saca desapila a partir del ultimo numero ingresado
        elif str(option)=="2":
                if len(stack) == 0:
                   print(" No hay elementos para desapilar ")
                   main()
                else:
                   print("El numero: ",stack.pop()," fue desapilado")
                   main()

        #Esta opcion imprime en pantalla la pila           
        elif str(option)=="3":
                for i in reversed(range(len(stack))):
                   print("Pila: ",stack[i])
                main()

        #Esta opcion permite salir de la ejecucion del codigo
        elif str(option)=="4":
                exit()
        else:
                print("\nOpcion incorrecta.\n")
                main()

main()
