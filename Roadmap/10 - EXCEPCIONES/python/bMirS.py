#EXCEPCIONES 
try:
    num=10/0
except Exception as e:
    print(f"Se tiene el siguiente error {e}") #Finally tiene que ejecutarse si o si
lista=[1,2,3]
try:
    print(lista[3])
except Exception as e:
    print(f" Se tiene el siguiente error {e}")

while True:
    try:
        edad=input("Ingresa tu edad: ")
        edad=int(edad)
        break
    except Exception as e:
        print(f"Intentelo de nuevo, Error:{e} ")
class Numeropar(Exception):
    pass
def ejercicioextra(lista, num):
    if len(lista)>5:
        raise IndexError("Rango esta fuera de limite ")
    if num == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    if num%2==0:
        raise  Numeropar("El numero es par")

try:
    ejercicioextra([1,2,3,4,5], 4)
    print(lista[2])
    print(10/num)
    print(num%2)
except IndexError:
    print("Error de rango")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except Numeropar:
    print("El numero es par, error")
print("Regresando al programa")