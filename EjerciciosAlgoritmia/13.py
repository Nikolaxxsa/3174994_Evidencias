#Menú con opciones del 6 al 12
#se importan librerias ramdom para generar numeros aleatorios
import random
lista = [random.randint(1, 100) for i in range(20)]
print(lista)
while True:
    print("\nMenú:")
    print("1. Buscar número")
    print("2. Contar apariciones")
    print("3. Número mayor y cuántas veces aparece")
    print("4. Verificar si aparece más que el mayor")
    print("5. Media de los números")
    print("6. Media entre el mayor y menor")
    print("7. Lista inversa")
    print("0. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        buscado = int(input("Número a buscar: "))
        i = 0
        encontrado = False
        while i < 20:
            if lista[i] == buscado:
                print("Encontrado en posición", i)
                encontrado = True
                break
            i = i + 1
        if not encontrado:
            print("No encontrado.")
    elif opcion == 2:
        buscado = int(input("Número a buscar: "))
        i = 0
        contador = 0
        while i < 20:
            if lista[i] == buscado:
                contador = contador + 1
            i = i + 1
        print("Aparece", contador, "veces.")
    elif opcion == 3:
        i = 0
        mayor = lista[0]
        while i < 20:
            if lista[i] > mayor:
                mayor = lista[i]
            i = i + 1
        i = 0
        contador = 0
        while i < 20:
            if lista[i] == mayor:
                contador = contador + 1
            i = i + 1
        print("Mayor:", mayor, "- Veces:", contador)
    elif opcion == 4:
        num = int(input("Número a evaluar: "))
        mayor = lista[0]
        i = 0
        while i < 20:
            if lista[i] > mayor:
                mayor = lista[i]
            i = i + 1
        cont_mayor = 0
        cont_num = 0
        i = 0
        while i < 20:
            if lista[i] == mayor:
                cont_mayor = cont_mayor + 1
            if lista[i] == num:
                cont_num = cont_num + 1
            i = i + 1
        if cont_num > cont_mayor:
            print("Verdadero")
        else:
            print("Falso")
    elif opcion == 5:
        suma = 0
        i = 0
        while i < 20:
            suma = suma + lista[i]
            i = i + 1
        print("Media:", suma / 20)
    elif opcion == 6:
        i = 0
        mayor = lista[0]
        menor = lista[0]
        while i < 20:
            if lista[i] > mayor:
                mayor = lista[i]
            if lista[i] < menor:
                menor = lista[i]
            i = i + 1
        print("Media entre mayor y menor:", (mayor + menor) / 2)
    elif opcion == 7:
        i = 19
        inversa = []
        while i >= 0:
            inversa.append(lista[i])
            i = i - 1
        print("Lista inversa:")
        i = 0
        while i < 20:
            print(inversa[i])
            i = i + 1
    elif opcion == 0:
        break
    else:
        print("Opción no válida.")
