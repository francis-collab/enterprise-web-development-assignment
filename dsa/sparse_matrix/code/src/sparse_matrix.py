class SparseMatrix:
    def __init__(self, file_path):
        self.matrix = {}  # Stores (row, col) -> value
        self.rows = 0
        self.cols = 0
        self.load_from_file(file_path)

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file.readlines() if line.strip()]  # Ignore empty lines

                # Validate format
                if not lines[0].startswith("rows=") or not lines[1].startswith("cols="):
                    raise ValueError("Input file has wrong format")

                self.rows = int(lines[0].split('=')[1])
                self.cols = int(lines[1].split('=')[1])

                for line in lines[2:]:
                    if not (line.startswith("(") and line.endswith(")")):
                        raise ValueError("Input file has wrong format")
                    row, col, value = map(int, line[1:-1].split(','))  # Extract data
                    self.matrix[(row, col)] = value

        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{file_path}' not found.")
        except Exception as e:
            raise ValueError(f"Error loading matrix: {e}")

    def get_element(self, row, col):
        return self.matrix.get((row, col), 0)  # Default to zero if absent

    def set_element(self, row, col, value):
        if value == 0 and (row, col) in self.matrix:
            del self.matrix[(row, col)]  # Remove zero entries to save memory
        elif value != 0:
            self.matrix[(row, col)] = value

