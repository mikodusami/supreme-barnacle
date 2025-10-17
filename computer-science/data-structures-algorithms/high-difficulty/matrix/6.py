from typing import List
import unittest

class Solution:
    def set_zeroes(self, matrix: List[List[int]]) -> None:
        """
        Sets entire row and column to 0 for each zero element in the matrix, in-place.
        
        Args:
            matrix: List[List[int]], m×n matrix
        Returns:
            None: Modifies matrix in-place
        
        Constraints:
            - 1 <= matrix.length, matrix[0].length <= 200
            - Target: O(m*n) time, O(1) space
        
        Possible Approaches:
            1. Use First Row/Column: Mark zeros in first row/column, then set zeros
            2. Store Indices: Use extra space to store zero rows/columns
            3. Brute Force: Mark cells to update later (uses extra space)
        """
        pass

class TestSetZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        self.solution.set_zeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_no_zeros(self):
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 2], [3, 4]]
        self.solution.set_zeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_single_element_zero(self):
        matrix = [[0]]
        expected = [[0]]
        self.solution.set_zeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_all_zeros(self):
        matrix = [[0, 0], [0, 0]]
        expected = [[0, 0], [0, 0]]
        self.solution.set_zeroes(matrix)
        self.assertEqual(matrix, expected)

if __name__ == "__main__":
    unittest.main()