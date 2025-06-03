#Contar cuántas veces aparece un número
#se importan librerias ramdom para generar numeros aleatorios
import random
lista = [random.randint(1, 100) for i in range(20)]
print(lista)

# Número que el usuario desea contar
buscado = int(input("Ingrese el número a buscar: "))

#Contador de ocurrencias
i = 0
contador = 0

# Bucle para recorrer la lista
while i < 20:
    if lista[i] == buscado:
        contador = contador + 1
    i = i + 1

# Se muestra cuántas veces aparece
print("El número aparece", contador, "veces.")