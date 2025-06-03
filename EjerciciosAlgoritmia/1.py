# Par o impar
numero = int(input("Ingrese un número: "))
# Se calcula el residuo de dividir el número entre 2
residuo = numero % 2
# Se evalúa si el residuo es cero
if residuo == 0:
    print("El número es par.")
else:
    print("El número es impar.")
