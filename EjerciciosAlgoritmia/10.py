#Media de la lista
#se importan librerias ramdom para generar numeros aleatorios
import random
lista = [random.randint(1, 100) for i in range(20)]
print(lista)
# Sumar todos los elementos
suma = 0
i = 0
while i < 20:
    suma = suma + lista[i]
    i = i + 1

# Calcular media
media = suma / 20

# Mostrar media
print("La media es:", media)