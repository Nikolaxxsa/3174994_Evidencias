# ¿Aparece más veces que el mayor?
#se importan librerias ramdom para generar numeros aleatorios
import random
lista = [random.randint(1, 100) for i in range(20)]
print(lista)
# Número a comparar
num = int(input("Ingrese un número: "))

# Buscar el número mayor
i = 0
mayor = lista[0]
while i < 20:
    if lista[i] > mayor:
        mayor = lista[i]
    i = i + 1

# Contar apariciones
cont_mayor = 0
cont_num = 0
i = 0
while i < 20:
    if lista[i] == mayor:
        cont_mayor = cont_mayor + 1
    if lista[i] == num:
        cont_num = cont_num + 1
    i = i + 1

# Comparar y mostrar
if cont_num > cont_mayor:
    print("Verdadero")
else:
    print("Falso")