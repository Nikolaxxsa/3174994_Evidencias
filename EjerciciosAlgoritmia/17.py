#Insertar aprendiz en lista ordenada
# Lista ordenada de apellidos
lista = ["Acuña", "Benítez", "Cardona", "Díaz", "Espitia", "Fernández", "Gómez", "Herrera", "Jiménez", "López"]

# Mostrar lista original
print("Lista original:")
i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1

# Ingresar nuevo apellido
nuevo = input("Ingrese el apellido del nuevo aprendiz: ")
lista.append(nuevo)  # Agregarlo a la lista

# Ordenar lista nuevamente usando burbuja
n = len(lista)
i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if lista[j] > lista[j + 1]:
            temp = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = temp
        j = j + 1
    i = i + 1

# Mostrar lista ordenada
print("Lista con nuevo aprendiz:")
i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1