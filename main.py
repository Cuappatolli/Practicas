import sys
import random

# Función para colocar los adoquines
def place(x1, y1, x2, y2, x3, y3):
    global cnt
    cnt += 1
    arr[x1][y1] = cnt
    arr[x2][y2] = cnt
    arr[x3][y3] = cnt

# Función recursiva para colocar los adoquines en la cuadrícula
def tile(n, x, y):
    global cnt
    r = 0
    c = 0
    # Caso base: si la cuadrícula es de 2x2, colocar adoquines y terminar
    if n == 2:
        cnt += 1
        for i in range(n):
            for j in range(n):
                if arr[x + i][y + j] == 0:
                    arr[x + i][y + j] = cnt
        return 0
    # Buscar una celda ocupada en la cuadrícula
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != 0:
                r = i
                c = j
    # Colocar adoquines de acuerdo a la posición de la celda ocupada
    if r < x + n / 2 and c < y + n / 2:
        place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2))
    elif r >= x + int(n / 2) and c < y + int(n / 2):
        place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2) - 1)
    elif r < x + int(n / 2) and c >= y + int(n / 2):
        place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2) - 1)
    elif r >= x + int(n / 2) and c >= y + int(n / 2):
        place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2) - 1, y + int(n / 2) - 1)
    # Llamar recursivamente a la función para cada cuadrante
    tile(int(n / 2), x, y + int(n / 2))
    tile(int(n / 2), x, y)
    tile(int(n / 2), x + int(n / 2), y)
    tile(int(n / 2), x + int(n / 2), y + int(n / 2))
    return 0

def main():
    # Obtener el tamaño de la cuadrícula desde la línea de comandos
    if len(sys.argv) != 2:
        print("Uso: python3 main.py <k>")
        return
    try:
        k = int(sys.argv[1])
        if k <= 0:
            raise ValueError
    except ValueError:
        print("Entrada inválida. Por favor proporciona un entero positivo")
        return

    # Calcular el tamaño de la cuadrícula
    size_of_grid = 2 ** k

    # Inicializar variables
    global cnt
    global arr
    cnt = 0
    arr = [[0 for i in range(size_of_grid)] for j in range(size_of_grid)]

    # Elegir una posición aleatoria para la casilla vacía
    empty_cell_x = random.randint(0, size_of_grid - 1)
    empty_cell_y = random.randint(0, size_of_grid - 1)
    arr[empty_cell_x][empty_cell_y] = -1

    # Llamar a la función tile para colocar los adoquines
    tile(size_of_grid, 0, 0)

    # Imprimir la cuadrícula resultante
    for i in range(size_of_grid):
        for j in range(size_of_grid):
            print(arr[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
