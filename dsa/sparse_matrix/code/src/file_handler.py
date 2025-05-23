# file_handler.py

from dsa.sparse_matrix.code.src.sparse_matrix import SparseMatrix

def read_matrix_from_file(file_path: str) -> SparseMatrix:
    try:
        with open(file_path, 'r') as f:
            numRows = None
            numCols = None
            matrix = None

            for i, line in enumerate(f):  # ✅ Stream file instead of loading entirely
                line = line.strip()
                if not line:
                    continue  # Ignore empty lines

                if i == 0:
                    numRows = int(line.split('=')[1].strip())
                elif i == 1:
                    numCols = int(line.split('=')[1].strip())
                    matrix = SparseMatrix(numRows, numCols)
                else:
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

                    # ✅ Column index validation fix
                    if row < 0 or row >= numRows or col < 0 or col > numCols - 1:
                        raise IndexError(f"Row or Column index out of bounds: ({row}, {col}). Expected range: 0 to {numCols - 1}")

                    matrix.setElement(row, col, val)

            return matrix

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")


def write_matrix_to_file(matrix: SparseMatrix, file_path: str):
    try:
        with open(file_path, 'w') as f:
            f.write(f"rows={matrix.numRows}\n")
            f.write(f"cols={matrix.numCols}\n")
            for row, col, val in matrix.getAllElements():
                f.write(f"({row}, {col}, {val})\n")
    except Exception as e:
        raise IOError(f"Error writing matrix to file: {e}")
