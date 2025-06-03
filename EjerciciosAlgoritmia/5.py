# Se crea una lista vacía para almacenar los números
numeros = []
i = 0

# Se piden cinco números al usuario
while i < 5:
    n = int(input("Ingrese un número: "))
    numeros.append(n)  # Se agrega el número a la lista
    i = i + 1

# Se ordena la lista usando el método burbuja (de mayor a menor)
j = 0
while j < 4:
    i = 0
    while i < 4 - j:
        if numeros[i] < numeros[i + 1]:  # Si el número actual es menor que el siguiente
            temp = numeros[i]  # Se intercambian
            numeros[i] = numeros[i + 1]
            numeros[i + 1] = temp
        i = i + 1
    j = j + 1

# Se muestra la lista ordenada
print("Números ordenados de mayor a menor:")
i = 0
while i < 5:
    print(numeros[i])
    i = i + 1
