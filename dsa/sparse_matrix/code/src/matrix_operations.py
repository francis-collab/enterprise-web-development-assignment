# matrix_operations.py

from sparse_matrix import SparseMatrix

def add_matrices(m1: SparseMatrix, m2: SparseMatrix) -> SparseMatrix:
    if m1.numRows != m2.numRows or m1.numCols != m2.numCols:
        raise ValueError("Matrix dimensions must match for addition")

    result = SparseMatrix(m1.numRows, m1.numCols)

    for row, col, val in m1.getAllElements():
        result.setElement(row, col, val)

    for row, col, val in m2.getAllElements():
        prev_val = result.getElement(row, col)
        result.setElement(row, col, prev_val + val)

    return result


def subtract_matrices(m1: SparseMatrix, m2: SparseMatrix) -> SparseMatrix:
    if m1.numRows != m2.numRows or m1.numCols != m2.numCols:
        raise ValueError("Matrix dimensions must match for subtraction")

    result = SparseMatrix(m1.numRows, m1.numCols)

    for row, col, val in m1.getAllElements():
        result.setElement(row, col, val)

    for row, col, val in m2.getAllElements():
        prev_val = result.getElement(row, col)
        result.setElement(row, col, prev_val - val)

    return result


def multiply_matrices(m1: SparseMatrix, m2: SparseMatrix) -> SparseMatrix:
    if m1.numCols != m2.numRows:
        raise ValueError("Matrix A columns must match Matrix B rows for multiplication")

    result = SparseMatrix(m1.numRows, m2.numCols)

    # Build a quick-access map for B
    b_map = {}
    for row, col, val in m2.getAllElements():
        if row not in b_map:
            b_map[row] = []
        b_map[row].append((col, val))

    for a_row, a_col, a_val in m1.getAllElements():
        if a_col in b_map:
            for b_col, b_val in b_map[a_col]:
                prev_val = result.getElement(a_row, b_col)
                result.setElement(a_row, b_col, prev_val + a_val * b_val)

    return result
