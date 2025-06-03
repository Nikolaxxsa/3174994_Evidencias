#Contar palabras y tamaño de la más larga
# Se pide al usuario un texto
texto = input("Ingrese un texto: ")

# Inicializar variables
i = 0
palabras = 0
tamano_mayor = 0
tam_actual = 0

# Recorrer el texto carácter por carácter
while i < len(texto):
    if texto[i] != " ":  # Si no es espacio, es parte de una palabra
        tam_actual = tam_actual + 1
    else:
        if tam_actual > 0:  # Se detectó una palabra
            palabras = palabras + 1
            if tam_actual > tamano_mayor:
                tamano_mayor = tam_actual
            tam_actual = 0
    i = i + 1

# Verificar última palabra si no terminó en espacio
if tam_actual > 0:
    palabras = palabras + 1
    if tam_actual > tamano_mayor:
        tamano_mayor = tam_actual

# Mostrar resultados
print("Número de palabras:", palabras)
print("Tamaño de la palabra más larga:", tamano_mayor)
