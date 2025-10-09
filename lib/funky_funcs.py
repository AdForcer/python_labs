def square_matrix_check(matrix: list[list[float | int]]) -> bool:
    width = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != width:
            return 0
    else:
        return 1
