import unittest
from sparse_matrix import SparseMatrix
from matrix_operations import add_matrices, subtract_matrices, multiply_matrices

class TestMatrixOperations(unittest.TestCase):
    def test_addition(self):
        matrixA = SparseMatrix("sample_inputs/matrixA.txt")
        matrixB = SparseMatrix("sample_inputs/matrixB.txt")
        result = add_matrices(matrixA, matrixB)

        self.assertEqual(result.get_element(0, 1), 5 + (-2))  # Expected sum

    def test_subtraction(self):
        matrixA = SparseMatrix("sample_inputs/matrixA.txt")
        matrixB = SparseMatrix("sample_inputs/matrixB.txt")
        result = subtract_matrices(matrixA, matrixB)

        self.assertEqual(result.get_element(0, 1), 5 - (-2))  # Expected difference

    def test_multiplication(self):
        matrixA = SparseMatrix("sample_inputs/matrixA.txt")
        matrixB = SparseMatrix("sample_inputs/matrixB.txt")
        result = multiply_matrices(matrixA, matrixB)

        # Verify known multiplication results based on matrix multiplication rules
        self.assertEqual(result.get_element(1, 2), matrixA.get_element(1, 2) * matrixB.get_element(2, 2))  

if __name__ == "__main__":
    unittest.main()

