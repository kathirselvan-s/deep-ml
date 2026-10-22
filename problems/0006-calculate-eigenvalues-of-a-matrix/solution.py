
import math

def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    a, b = matrix[0]
    c, d = matrix[1]

    trace = a + d
    determinant = a * d - b * c
    dis = trace**2 - 4 * determinant

    if dis < 0:
        raise ValueError("Matrix has complex eigenvalues")

    e1 = (trace + math.sqrt(dis)) / 2
    e2 = (trace - math.sqrt(dis)) / 2

    e = [float(e1), float(e2)]
    e.sort(reverse=True)

    return e
