import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    rows = len(a)
    cols = len(a[0]) if rows > 0 else 0

    if rows * cols != new_shape[0] * new_shape[1]:
        return []

    result = []
    row = []

    for i in range(rows):
        for j in range(cols):
            row.append(a[i][j])

            if len(row) == new_shape[1]:
                result.append(row)
                row = []

    return result