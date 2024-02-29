import random
from typing import List


def bubble_sort(arr: List[List]) -> None:
    n = len(arr)

    for _ in range(n - 1):
        swapped = False

        for i in range(n - 1):
            if arr[i][1] > arr[i + 1][1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
            break

def quick_sort(arr: List[List], left: int, right: int) -> None:
    if left >= right:
        return

    pivot = arr[(left + right) // 2][1]
    i = left - 1
    j = right + 1
    while True:
        while arr[i][1] < pivot:
            i += 1
        while arr[j - 1][1] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j - 1] = arr[j - 1], arr[i]
        i, j = i + 1, j - 1

        arr[j], arr[right] = arr[right], arr[j]


def ordenar_fila(matrix: List[List], fila: int) -> List[List]:
    """Ordena la fila 'fila' de la matriz 'matrix' mediante algún método de ordenamiento."""
    new_row = list(matrix[fila])
    MATRIX_SIZE = 3
    matriz = [[random.randint(1, 9) for _ in range(MATRIX_SIZE)] for _ in range(MATRIZ_SIZE)]
    fila_especifica = 1
    matriz_original = matriz[:]
    matriz_ordenada = ordenar_fila(matriz, fila_especifica)

    print("\nMatriz Original:\n")
    for fila in matriz_original:
        print(*fila)

    print("\n\nFila {} ordenada:\n".format(fila_especifico))
    for fila in matriz_ordenada:
        print(*fila)