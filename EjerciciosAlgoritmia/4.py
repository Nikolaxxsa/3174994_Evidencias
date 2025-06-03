# Se ingresan dos números por teclado
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

# Se asegura que 'inicio' sea menor que 'fin'
if inicio > fin:
    temp = inicio
    inicio = fin
    fin = temp

# Se inicializa la suma
suma = 0

# Se recorre el rango desde inicio hasta fin
i = inicio
while i <= fin:
    if i % 2 == 0:  # Si el número es par
        suma = suma + i  # Se suma al acumulador
    i = i + 1  # Se incrementa i

# Se imprime el resultado
print("La suma de los pares es:", suma)
