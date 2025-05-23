import unittest
from sparse_matrix import SparseMatrix

class TestSparseMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = SparseMatrix(10, 10)

    def test_set_and_get_element(self):
        self.matrix.setElement(3, 5, 42)
        self.assertEqual(self.matrix.getElement(3, 5), 42)

    def test_get_default_zero(self):
        self.assertEqual(self.matrix.getElement(2, 2), 0)

    def test_remove_element(self):
        self.matrix.setElement(4, 6, 99)
        self.matrix.setElement(4, 6, 0)  # Remove it
        self.assertEqual(self.matrix.getElement(4, 6), 0)

if __name__ == '__main__':
    unittest.main()
