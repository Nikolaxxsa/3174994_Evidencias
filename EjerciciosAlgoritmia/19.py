#Contar cifras de un número
# Pedir número entero al usuario
numero = int(input("Ingrese un número entero: "))

# Si es cero, tiene una sola cifra
if numero == 0:
    print("Cantidad de cifras: 1")
else:
    cifras = 0
    if numero < 0:
        numero = -numero  # Convertir a positivo
    while numero > 0:
        numero = numero // 10  # Quitar una cifra
        cifras = cifras + 1  # Contador de cifras
    print("Cantidad de cifras:", cifras)