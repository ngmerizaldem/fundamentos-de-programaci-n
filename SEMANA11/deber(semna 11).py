
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"El valor {valor} se encontró en la posición ({i}, {j}) de la matriz."
    return f"El valor {valor} no se encontró en la matriz."
valor_buscado = 5
resultado = buscar_valor(matriz, valor_buscado)
print(resultado)