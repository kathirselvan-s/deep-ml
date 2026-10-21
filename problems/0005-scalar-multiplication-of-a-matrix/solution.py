
def scalar_multiply(matrix: list[list[int | float]], scalar: int | float) -> list[list[int | float]]:
    result = []
    for row in matrix:
        row_n = []
        for i in row:
            row_n.append(i* scalar)
        result.append(row_n)
    return result

