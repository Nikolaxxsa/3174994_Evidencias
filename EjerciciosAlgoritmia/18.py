#Calcular letra del NIT
# Tabla de letras asociadas al resto de NIT % 23
tabla = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
         "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

# Solicitar número del NIT
nit = int(input("Ingrese el número NIT: "))

# Calcular la letra usando el módulo 23
resto = nit % 23
print("Letra de control:", tabla[resto])