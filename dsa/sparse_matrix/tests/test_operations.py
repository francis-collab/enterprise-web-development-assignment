import unittest
from dsa.sparse_matrix.code.src.sparse_matrix import SparseMatrix
from dsa.sparse_matrix.code.src.matrix_operations import add_matrices, subtract_matrices, multiply_matrices

class TestMatrixOperations(unittest.TestCase):
    def setUp(self):
        self.matrixA = SparseMatrix(3, 3)
        self.matrixB = SparseMatrix(3, 3)
        self.matrixA.setElement(0, 1, 5)
        self.matrixB.setElement(0, 1, 3)

    def test_add_matrices(self):
        result = add_matrices(self.matrixA, self.matrixB)
        self.assertEqual(result.getElement(0, 1), 8)

    def test_subtract_matrices(self):
        result = subtract_matrices(self.matrixA, self.matrixB)
        self.assertEqual(result.getElement(0, 1), 2)

    def test_multiply_matrices(self):
        matrixC = SparseMatrix(3, 3)
        matrixC.setElement(1, 2, 4)
        result = multiply_matrices(self.matrixA, matrixC)
        self.assertEqual(result.getElement(0, 2), 20)  # 5 * 4

if __name__ == '__main__':
    unittest.main()
