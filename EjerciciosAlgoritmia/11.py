#Media entre el mayor y el menor
#se importan librerias ramdom para generar numeros aleatorios
import random
lista = [random.randint(1, 100) for i in range(20)]
print(lista)
# Inicializar mayor y menor con el primer valor de la lista
i = 0
mayor = lista[0]
menor = lista[0]

# Recorrer la lista para encontrar mayor y menor
while i < 20:
    if lista[i] > mayor:
        mayor = lista[i]
    if lista[i] < menor:
        menor = lista[i]
    i = i + 1

# Calcular la media entre ambos
media = (mayor + menor) / 2

# Mostrar resultado
print("Media entre el mayor y el menor:", media)