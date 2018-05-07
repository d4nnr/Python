#/usr/bin/env python

stack = []

def main():
        print("1 Aplilar elemento (entero)")
        print("2 Desapilar elemento")
        print("3 Mostrar pila")
        print("4 Salir")
        option = input("Elija una opcion: ")

        if str(option)=="1":
                elemento = input(" Introduzca el numero a apilar: ")
                stack.append(elemento)
                print(" Elemento apilado ")
                main()

        elif str(option)=="2":
                if len(stack) == 0:
                   print(" No hay elementos para desapilar ")
                   main()
                else:
                   print("El numero: ",stack.pop()," fue desapilado")
                   main()

        elif str(option)=="3":
                for i in reversed(range(len(stack))):
                   print("Pila: ",stack[i])
                main()

        elif str(option)=="4":
                        exit()
        else:
                print("\nOpcion incorrecta.\n")
                main()

main()
