# Busca un número en una lista de 20 números aleatorios
#se importan librerias ramdom para generar numeros aleatorios
import random
lista = [random.randint(1, 100) for i in range(20)]
print("Lista:", lista)
# Se solicita el número a buscar
buscado = int(input("Ingrese el número a buscar: "))

# Inicialización del índice y la bandera
i = 0
encontrado = False

# Bucle para buscar el número en la lista
while i < 20:
    if lista[i] == buscado:  # Si lo encuentra
        print("Número encontrado en la posición", i)
        encontrado = True
        break  # Sale del bucle
    i = i + 1

# Si no lo encontró
if not encontrado:
    print("Número no encontrado.")