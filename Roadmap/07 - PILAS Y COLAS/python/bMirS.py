#PILAS EL ULTIMO EN ENTRAR ES EL PRIMERO EN SALIR
pila=[]
cola=[]
#Agregar cosas a las pilas
pila.append("lugar1")
pila.append("lugar2")
def apilar(elemento:str, pila:list):
    return pila.append(elemento)
def encolar(elemento:str, pila:list):
    return pila.append(elemento)
def desapilar():
    if len(pila)==0:
        print("La pila esta vacia ")
    else:
       return pila.pop()
def desencolar ():
    if len(cola)==0:
        print("La cola esta vacia")
    else:
        return cola.pop(0) #ME DICE LO QUE BORRO 

while  True:

    print("1. Apilar ")
    print("2. Desapilar")
    print("3. Encolar ")
    print("4. Desencolar ")
    print("5. Salir")
    opc=int(input("Ingresa la opción: "))

    match opc:
        case 1:
        #EN DONDE CREO LA LISTA 
            
            elemento=input("Ingresa el elemento para apilar: ")
            apilar(elemento, pila)
            print(pila)
        case 2:
            if len(pila)==0:
               print("No hay elementos") 
            else:
                print(f"El elemento a desapilar es {desapilar()}")
        case 3:
            elemento=input("Ingresa el elemento para encolar: ")
            encolar(elemento, cola)
            print(cola)
           
        case 4:
            if len(cola)==0:
                print("No hay elementos para desapilar")
            else:
                print(f"El elemento desencolado es {desencolar()} ")
              
            print(cola)
        case 5:
            break
        case _:
            print("Ingresa una opcion valida")
#LINEA