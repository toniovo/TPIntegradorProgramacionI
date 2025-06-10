def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Inicio del programa
print("---- Algoritmos de Búsqueda y Ordenamiento ----")

# Ingreso de números
entrada = input("Ingrese números separados por comas: ")
datos = [int(x.strip()) for x in entrada.split(",")]
print("Lista ingresada:", datos)

# Elección del método de ordenamiento
print("Métodos de ordenamiento disponibles:")
print("1. Bubble Sort")
print("2. Selection Sort")
op_orden = input("Seleccione una opción (1 o 2): ")

if op_orden == "1":
    datos_ordenados = bubble_sort(datos.copy())
    print("Lista ordenada con Bubble Sort:", datos_ordenados)
elif op_orden == "2":
    datos_ordenados = selection_sort(datos.copy())
    print("Lista ordenada con Selection Sort:", datos_ordenados)
else:
    print("Opción inválida. Se ordenará con Bubble Sort por defecto.")
    datos_ordenados = bubble_sort(datos.copy())

# Ingreso del número a buscar
buscar = int(input("Ingrese el número que desea buscar: "))

# Elección del método de búsqueda
print("Métodos de búsqueda disponibles:")
print("1. Búsqueda Lineal")
print("2. Búsqueda Binaria")
op_busqueda = input("Seleccione una opción (1 o 2): ")

if op_busqueda == "1":
    resultado = linear_search(datos_ordenados, buscar)
    metodo = "Búsqueda Lineal"
elif op_busqueda == "2":
    resultado = binary_search(datos_ordenados, buscar)
    metodo = "Búsqueda Binaria"
else:
    print("Opción inválida. Se usará Búsqueda Lineal por defecto.")
    resultado = linear_search(datos_ordenados, buscar)
    metodo = "Búsqueda Lineal"

# Resultado búsqueda
if resultado != -1:
    print(f"[{metodo}] El número {buscar} se encuentra en la posición {resultado}.")
else:
    print(f"[{metodo}] El número {buscar} no fue encontrado en la lista.")
