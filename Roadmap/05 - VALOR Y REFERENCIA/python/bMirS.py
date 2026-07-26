variable1=5
variable2=6
variable2=variable1
variable1=10 #Cambio el valor de variable 1
print(variable1) 
print(variable2)#valor no se modifica

lista1=["1", "2", "3", "4"]
lista2=lista1
lista2.append("50")
print("Lista original sin modificar",lista1)
print("Lista 2 modificada", lista2)

def  pasoporvalor(numero:int):
    numero=10
numero=15
pasoporvalor(numero)
print(numero) #no se cambio el valor

def pasoreferencia(lista:list):
    lista.append(1)
lista=[5,6,7]
pasoreferencia(lista)
print(lista) #se agrega 1 a la lista

def funcion1porvalor(entero1:int, entero2:int):
    tem=entero2
    entero2=entero1
    entero1=tem

    return entero1, entero2
entero1=5
entero2=10
nuevo1,nuevo2=funcion1porvalor(entero1, entero2)
print("Variables nuevas")
print(f"Var 1: {nuevo1} Var 2: {nuevo2}")
print("Variables originales con valores 5,10")
print(entero1)
print(entero2)
def funporreferencia(lista1:list, lista2:list):
    listatem=lista1
    lista1=lista2
    lista2=listatem
    return lista1, lista2
lista1=["2","4","6"]
lista2=["3","5","7"]
copiar1, copiar2= funporreferencia(lista1, lista2)
print(f"Originales {lista1}  y {lista2} ")
print(f"Invertidos {copiar1}  y {copiar2} ")
