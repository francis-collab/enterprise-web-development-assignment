import unittest
from sparse_matrix import SparseMatrix

class TestSparseMatrix(unittest.TestCase):
    def test_loading_matrix(self):
        matrix = SparseMatrix("sample_inputs/matrixA.txt")
        self.assertEqual(matrix.get_element(0, 1), 5)

    def test_missing_element_returns_zero(self):
        matrix = SparseMatrix("sample_inputs/matrixA.txt")
        self.assertEqual(matrix.get_element(2, 2), 0)

if __name__ == "__main__":
    unittest.main()
