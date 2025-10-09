def square_matrix_check(matrix: list[list[float | int]]) -> bool:

    width = len(matrix[0])

    for i in range(len(matrix)):
        if len(matrix[i]) != width:
            return 0
    else:
        return 1

def transpose(mat: list[list[float | int]]) -> list[list]:

    if square_matrix_check(mat) == 0:
        return "ValueError"
    
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]

print("Тесты transpose")
print(transpose([[1, 2, 3]]))  # [[1], [2], [3]]
print(transpose([[1], [2], [3]]))  # [[1, 2, 3]]
print(transpose([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
print(transpose([[1, 2], [3]]))

def row_sums(mat: list[list[float | int]]) -> list[float]:

    if square_matrix_check(mat) == 0:
        return "ValueError"
    
    return [sum(row) for row in mat]

print("\nТесты row_sums")
print(row_sums([[1, 2, 3], [4, 5, 6]]))  # [6, 15]
print(row_sums([[-1, 1], [10, -10]]))  # [0, 0]
print(row_sums([[0, 0], [0, 0]]))  # [0, 0]
print(row_sums([[1, 2], [3]]))

def col_sums(mat: list[list[float | int]]) -> list[float]:

    if square_matrix_check(mat) == 0:
        return "ValueError"
    
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]

print("\nТесты col_sums:")
print(col_sums([[1, 2, 3], [4, 5, 6]]))  # [5, 7, 9]
print(col_sums([[-1, 1], [10, -10]]))  # [9, -9]
print(col_sums([[0, 0], [0, 0]]))  # [0, 0]
print(col_sums([[1, 2], [3]]))