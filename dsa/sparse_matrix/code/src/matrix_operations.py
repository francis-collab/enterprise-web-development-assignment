def add_matrices(matrix1, matrix2):
    if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
        raise ValueError("Matrices must have the same dimensions for addition.")

    result = SparseMatrix(matrix1.rows, matrix1.cols)
    for (row, col), value in matrix1.matrix.items():
        result.matrix[(row, col)] = value

    for (row, col), value in matrix2.matrix.items():
        result.matrix[(row, col)] = result.get_element(row, col) + value

    return result

def subtract_matrices(matrix1, matrix2):
    if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
        raise ValueError("Matrices must have the same dimensions for subtraction.")

    result = SparseMatrix(matrix1.rows, matrix1.cols)
    for (row, col), value in matrix1.matrix.items():
        result.matrix[(row, col)] = value

    for (row, col), value in matrix2.matrix.items():
        result.matrix[(row, col)] = result.get_element(row, col) - value

    return result

def multiply_matrices(matrix1, matrix2):
    if matrix1.cols != matrix2.rows:
        raise ValueError("Invalid matrix dimensions for multiplication.")

    result = SparseMatrix(matrix1.rows, matrix2.cols)

    for (rowA, colA), valueA in matrix1.matrix.items():
        for colB in range(matrix2.cols):
            valueB = matrix2.get_element(colA, colB)
            if valueB != 0:
                result.matrix[(rowA, colB)] = result.get_element(rowA, colB) + (valueA * valueB)

    return result

