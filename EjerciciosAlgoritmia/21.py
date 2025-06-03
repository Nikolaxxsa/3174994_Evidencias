#Juego Rojo-Amarillo-Verde
import random  # Importar para usar números aleatorios

# Generar tres dígitos aleatorios únicos
valores = []
while len(valores) < 3:
    valor = random.randint(0, 9)
    i = 0
    repetido = False
    while i < len(valores):
        if valores[i] == valor:
            repetido = True
            break
        i = i + 1
    if not repetido:
        valores.append(valor)

# Juego de adivinanza
intentos = 0
while True:
    print("\nIntento", intentos + 1)
    a = int(input("Dígito posición 1: "))
    b = int(input("Dígito posición 2: "))
    c = int(input("Dígito posición 3: "))
    intento = [a, b, c]

    colores = []  # Lista para las pistas
    i = 0
    while i < 3:
        if intento[i] == valores[i]:
            colores.append("verde")  # Correcto en la posición
        else:
            j = 0
            esta = False
            while j < 3:
                if intento[i] == valores[j] and i != j:
                    esta = True
                j = j + 1
            if esta:
                colores.append("amarillo")  # Está pero en posición incorrecta
            else:
                colores.append("rojo")  # No está
        i = i + 1

    print("Pista:", colores[0], colores[1], colores[2])

    # Si todos son verdes, el juego termina
    if colores[0] == "verde" and colores[1] == "verde" and colores[2] == "verde":
        print("¡Ganaste en", intentos + 1, "intentos!")
        break

    intentos = intentos + 1