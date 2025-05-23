from sparse_matrix import SparseMatrix

def read_matrix_from_file(file_path: str) -> SparseMatrix:
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    if len(lines) < 2:
        raise ValueError("Input file is too short or missing rows/cols definition")

    try:
        numRows = int(lines[0].split('=')[1].strip())
        numCols = int(lines[1].split('=')[1].strip())
    except:
        raise ValueError("Invalid rows/cols format")

    matrix = SparseMatrix(numRows, numCols)

    for line in lines[2:]:
        line = line.strip()
        if not line:
            continue

        if not (line.startswith('(') and line.endswith(')')):
            raise ValueError("Input file has wrong format: missing valid parentheses")

        contents = line[1:-1].split(',')
        if len(contents) != 3:
            raise ValueError("Input file has wrong format: coordinate entry invalid")

        try:
            row = int(contents[0].strip())
            col = int(contents[1].strip())
            val = int(contents[2].strip())
        except ValueError:
            raise ValueError("Input file has wrong format: entries must be integers")

        row -= 1
        col -= 1

        print(f"Parsed indices (before adjusting): row={row+1}, col={col+1}")
        print(f"Adjusted indices (0-based): row={row}, col={col}")
        print(f"Matrix dimensions: rows={numRows}, cols={numCols}")

        if row < 0 or row >= numRows or col < 0 or col >= numCols:
            raise IndexError(f"Row or Column index out of bounds: ({row+1}, {col+1})")

        matrix.setElement(row, col, val)

    return matrix


def write_matrix_to_file(matrix: SparseMatrix, file_path: str):
    with open(file_path, 'w') as f:
        f.write(f"rows={matrix.numRows}\n")
        f.write(f"cols={matrix.numCols}\n")
        for row, col, val in matrix.getAllElements():
            f.write(f"({row}, {col}, {val})\n")
