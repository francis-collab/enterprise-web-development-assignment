def write_matrix_to_file(matrix, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(f"rows={matrix.rows}\n")
            file.write(f"cols={matrix.cols}\n")

            for (row, col), value in matrix.matrix.items():
                file.write(f"({row}, {col}, {value})\n")

    except Exception as e:
        print("Error writing matrix to file:", e)
