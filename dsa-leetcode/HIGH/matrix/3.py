from typing import List
import unittest

class Solution:
    def diagonal_sum(self, matrix: List[List[int]]) -> int:
        """
        Calculates the sum of elements in primary and secondary diagonals of a square matrix.
        Elements on both diagonals are counted once.
        
        Args:
            matrix: List[List[int]], n×n square matrix
        Returns:
            int: Sum of diagonal elements
        
        Constraints:
            - matrix.length == matrix[0].length
            - 1 <= matrix.length <= 100
            - Target: O(n) time, O(1) space
        
        Possible Approaches:
            1. Single Pass: Iterate over matrix, add diagonal elements
            2. Two Passes: Sum primary and secondary diagonals separately
            3. Brute Force: Check all elements for diagonal positions
        """
        pass

class TestDiagonalSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.solution.diagonal_sum(matrix), 25)

    def test_single_element(self):
        matrix = [[5]]
        self.assertEqual(self.solution.diagonal_sum(matrix), 5)

    def test_2x2_matrix(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(self.solution.diagonal_sum(matrix), 10)

    def test_4x4_matrix(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.assertEqual(self.solution.diagonal_sum(matrix), 34)

if __name__ == "__main__":
    unittest.main()