import unittest
from sparse_matrix import SparseMatrix
from file_handler import write_matrix_to_file

class TestFileHandler(unittest.TestCase):
    def test_reading_matrix(self):
        matrix = SparseMatrix("/dsa/sparse_matrix/sample_inputs/matrixA.txt")
        self.assertEqual(matrix.get_element(0, 1), 5)  # Expected value in matrixA

    def test_writing_matrix(self):
        matrix = SparseMatrix("/dsa/sparse_matrix/sample_inputs/matrixA.txt")
        write_matrix_to_file(matrix, "/dsa/sparse_matrix/sample_outputs/test_output.txt")
        
        # Re-load written file and verify integrity
        written_matrix = SparseMatrix("/dsa/sparse_matrix/sample_outputs/test_output.txt")
        self.assertEqual(written_matrix.get_element(0, 1), 5)

if __name__ == "__main__":
    unittest.main()
