#Calcular cambio con monedas
# Ingresar el valor a cobrar y el monto entregado
cobro = int(input("Valor a cobrar: "))
pagado = int(input("Monto entregado: "))

# Calcular la cantidad de cambio
cambio = pagado - cobro
print("Cambio a devolver:", cambio)

# Lista de monedas disponibles (de mayor a menor)
monedas = [1000, 500, 200, 100, 50]

# Recorremos las monedas para calcular cuántas se necesitan
i = 0
while i < 5:
    cantidad = cambio // monedas[i]  # Cuántas monedas de este valor caben
    if cantidad > 0:
        print(monedas[i], "x", cantidad)  # Mostrar cuántas monedas de ese valor
    cambio = cambio - cantidad * monedas[i]  # Reducir el cambio restante
    i = i + 1