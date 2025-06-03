# Mayor y cuántas veces aparece
#se importan librerias ramdom para generar numeros aleatorios
import random
lista = [random.randint(1, 100) for i in range(20)]
print(lista)
# Buscar el número mayor
i = 0
mayor = lista[0]
while i < 20:
    if lista[i] > mayor:
        mayor = lista[i]
    i = i + 1

# Contar cuántas veces aparece el mayor
contador = 0
i = 0
while i < 20:
    if lista[i] == mayor:
        contador = contador + 1
    i = i + 1

# Mostrar resultados
print("El número mayor es:", mayor)
print("Aparece", contador, "veces.")