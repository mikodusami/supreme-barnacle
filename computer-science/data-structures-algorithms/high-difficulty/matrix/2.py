from typing import List
import unittest

class Solution:
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Determines if a target value exists in a sorted m×n matrix.
        
        Args:
            matrix: List[List[int]], sorted m×n matrix (row-wise and column-wise)
            target: int, value to find
        Returns:
            bool: True if target exists, False otherwise
        
        Constraints:
            - 1 <= matrix.length, matrix[0].length <= 100
            - Matrix is sorted in ascending order
            - Target: O(log(m*n)) time, O(1) space
        
        Possible Approaches:
            1. Binary Search: Treat matrix as flattened sorted array
            2. Two-Step Binary Search: Search row first, then column
            3. Linear Search from Top-Right: Eliminate rows or columns
        """
        pass

class TestSearchMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 16
        self.assertTrue(self.solution.search_matrix(matrix, target))

    def test_target_not_found(self):
        matrix = [[1, 3, 5], [10, 11, 16]]
        target = 12
        self.assertFalse(self.solution.search_matrix(matrix, target))

    def test_single_element(self):
        matrix = [[1]]
        target = 1
        self.assertTrue(self.solution.search_matrix(matrix, target))

    def test_empty_matrix(self):
        matrix = []
        target = 1
        self.assertFalse(self.solution.search_matrix(matrix, target))

if __name__ == "__main__":
    unittest.main()