#Cálculo de la cuota mensual de una hipoteca
# Entrada de datos
C = float(input("Capital del préstamo: "))  # Capital
interes_anual = float(input("Interés anual (%): "))  # Interés
anios = int(input("Número de años: "))  # Tiempo en años

# Cálculo del interés mensual y número total de cuotas
R = interes_anual / 100 / 12  # Tasa mensual
N = anios * 12  # Total de pagos

# Cálculo de (1 + R)^N
potencia = 1
i = 0
while i < N:
    potencia = potencia * (1 + R)
    i = i + 1

# Aplicación de fórmula para cuota mensual
denominador = 1 - (1 / potencia)
cuota = C * R / denominador

# Mostrar resultados
print("Cuota mensual:", cuota)
print("Total a pagar:", cuota * N)