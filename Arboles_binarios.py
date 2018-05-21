############################################
############################################
##  Autor:   Daniel Romo Garcia           ##
##  Email:   danielromogarcia@gmail.com   ##
##  Blog:    d4nnr.blogspot.com           ##
##  Twitter: @d4nnr                       ##
############################################
############################################

#Clase llamada nodo
class Nodo:
    #Constructor con los argumentos
    def __init__(self, value=None, izq=None, der=None):
        #Punteros
        self.value = value
        self.izq = izq
        self.der = der

    #Retornar el valor
    def __str__(self):
        return self.value

#Clase del arbol binario
class aBinarios:
    #metodo constructor y el atributo raiz
    def __init__(self):
        self.raiz = None
    #creamos la funcion agregar
    def agregar(self, elemento):

        if self.raiz == None:
            self.raiz = elemento
        else:
            aux = self.raiz
            padre = None
            while aux != None:
                padre = aux
                if int(elemento.value) >= int(aux.value): 
                    aux = aux.der
                else:
                    aux = aux.izq
            if int(elemento.value) >= int(padre.value):
                padre.der = elemento
            else:
                padre.izq = elemento

    #se crea metodo mostrar el preorden
    def preorden(self, elemento):
        if elemento != None:
            print(elemento)
            self.preorden(elemento.izq)
            self.preorden(elemento.der)

    #se crea metodo mostrar el posrden (recursividad)
    def postorden(self, elemento):
        if elemento != None:
            self.postorden(elemento.izq)
            self.postorden(elemento.der)
            print(elemento)

    #se crea metodo mostrar el inorden
    def inorden(self, elemento):
        if elemento != None:
            self.inorden(elemento.izq)
            print(elemento)
            self.inorden(elemento.der)

    #se crea funcion que permite obtener la reiz
    def getRaiz(self):
        return self.raiz

#creamos un menu
if __name__ == "__main__":
    #llamamos el objeto de arbol binario
    ab = aBinarios()
    while(True):
        #opciones del menu
        print("Arboles_Binarios\n"+
            "1. Agregar\n"+
            "2. Preorden\n"+
            "3. Postorden\n"+
            "4. Inorden\n"+
            "5. Salir")

        num = input("ingrese la opcion")

        if num == "1":
            value = input("Ingrese el valor: ")
            nod =Nodo(value)
            ab.agregar(nod)

        elif num == "2":
            print("Preorden")
            ab.preorden(ab.getRaiz())
        elif num == "3":
            print("postorden")
            ab.postorden(ab.getRaiz())
        elif num == "4":
            print("inorden")
            ab.inorden(ab.getRaiz())
        elif num == "5":
            exit() 
