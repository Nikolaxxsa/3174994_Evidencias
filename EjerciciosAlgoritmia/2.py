#Suma de 1 a N
# Se solicita al usuario un número entero positivo
N = int(input("Ingrese un número N: "))
# Se inicializa una variable para acumular la suma
suma = 0
# Se inicializa el contador
i = 1
# Bucle que va sumando los números del 1 al N
while i <= N:
    suma = suma + i
    i = i + 1
    
# Se muestra el resultado final
print("La suma es:", suma)
