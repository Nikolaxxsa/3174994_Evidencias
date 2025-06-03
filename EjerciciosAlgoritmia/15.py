#Año bisiesto
# Se ingresa un año
anio = int(input("Ingrese un año: "))

# Aplicar las reglas del año bisiesto
if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print("Es bisiesto.")  # Divisible entre 400
        else:
            print("No es bisiesto.")  # Divisible entre 100 pero no entre 400
    else:
        print("Es bisiesto.")  # Divisible entre 4 pero no entre 100
else:
    print("No es bisiesto.")  # No divisible entre 4