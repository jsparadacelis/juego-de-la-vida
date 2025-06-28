from time import sleep
import os

INITIAL_MATRIX = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def print_matrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        print(" ".join(str(cell) for cell in row))
    print("\n")


def calculate_alive_neighbors(matrix: list[list[int]], pos: tuple[int, int]) -> int:
    alive_neighbors = 0

    if pos == (0, 0):
        for k in matrix[0 : pos[0] + 2]:
            for j in k[0 : pos[1] + 2]:
                if j == 1:
                    alive_neighbors += 1

    elif pos[0] == 0:
        for k in matrix[0 : pos[0] + 2]:
            for j in k[pos[1] - 1 : pos[1] + 2]:
                if j == 1:
                    alive_neighbors += 1

    elif pos[1] == 0:
        for k in matrix[pos[0] - 1 : pos[0] + 2]:
            for j in k[0 : pos[1] + 2]:
                if j == 1:
                    alive_neighbors += 1

    else:
        for k in matrix[pos[0] - 1 : pos[0] + 2]:
            for j in k[pos[1] - 1 : pos[1] + 2]:
                if j == 1:
                    alive_neighbors += 1

    if matrix[pos[0]][pos[1]] == 1:
        alive_neighbors = alive_neighbors - 1

    return alive_neighbors


def generate_new_matrix(matrix: list[list[int]]) -> list[list[int]]:
    alive_neighbors = 0
    
    row_number = len(matrix)
    col_number = len(matrix[0])

    new_matrix = [[0 for _ in range(col_number)] for _ in range(row_number)]

    for i in range(row_number):
        for j in range(col_number):

            current_pos = (i, j)
            current_value = matrix[i][j]
            alive_neighbors = calculate_alive_neighbors(matrix, current_pos)

            if current_value == 0 and alive_neighbors == 3:
                new_matrix[i][j] = 1

            elif current_value == 1 and alive_neighbors < 2:
                new_matrix[i][j] = 0

            elif current_value == 1 and alive_neighbors > 3:
                new_matrix[i][j] = 0

            elif current_value == 1 and (alive_neighbors == 2 or alive_neighbors == 3):
                new_matrix[i][j] = 1

    return new_matrix


def main():
    matrix = INITIAL_MATRIX
    while True:
        try:
            os.system("clear")
            print_matrix(matrix)
            matrix = generate_new_matrix(matrix)
            sleep(0.5)
        except KeyboardInterrupt:
            print("Finishing the game...")
            break

if __name__ == "__main__":
    main()
