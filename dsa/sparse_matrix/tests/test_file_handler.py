import unittest
import os
from file_handler import read_matrix_from_file, write_matrix_to_file
from sparse_matrix import SparseMatrix

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_matrix.txt"
        with open(self.test_file, "w") as f:
            f.write("rows=5\ncols=5\n(1, 2, 10)\n(3, 4, -7)")

    def test_read_matrix_from_file(self):
        matrix = read_matrix_from_file(self.test_file)
        self.assertEqual(matrix.getElement(1, 2), 10)
        self.assertEqual(matrix.getElement(3, 4), -7)

    def test_write_matrix_to_file(self):
        matrix = SparseMatrix(5, 5)
        matrix.setElement(2, 3, 6)
        write_matrix_to_file(matrix, self.test_file)

        with open(self.test_file, "r") as f:
            data = f.readlines()

        self.assertIn("(2, 3, 6)\n", data)

    def tearDown(self):
        os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()
