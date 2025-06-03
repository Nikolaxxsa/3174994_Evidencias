# Lista inversa
#se importan librerias ramdom para generar numeros aleatorios
import random
lista = [random.randint(1, 100) for i in range(20)]
print(lista)
# Lista nueva para guardar en orden inverso
inversa = []

# Recorrer la lista al revés
i = 19
while i >= 0:
    inversa.append(lista[i])  # Añadir al final de la lista inversa
    i = i - 1

# Imprimir la lista inversa
print("Lista inversa:")
i = 0
while i < 20:
    print(inversa[i])
    i = i + 1