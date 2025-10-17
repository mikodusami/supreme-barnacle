from typing import List
import unittest

class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        """
        Returns a list of matrix elements in spiral order (clockwise from top-left).
        
        Args:
            matrix: List[List[int]], m×n matrix
        Returns:
            List[int]: Elements in spiral order
        
        Constraints:
            - 1 <= matrix.length, matrix[0].length <= 100
            - Target: O(m*n) time, O(1) space (excluding output)
        
        Possible Approaches:
            1. Layer by Layer: Process boundaries in spiral order
            2. Direction-Based: Use direction pointers to traverse
            3. Brute Force: Mark visited cells and navigate (uses extra space)
        """
        pass

class TestSpiralOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.solution.spiral_order(matrix), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_single_element(self):
        matrix = [[1]]
        self.assertEqual(self.solution.spiral_order(matrix), [1])

    def test_single_row(self):
        matrix = [[1, 2, 3]]
        self.assertEqual(self.solution.spiral_order(matrix), [1, 2, 3])

    def test_single_column(self):
        matrix = [[1], [2], [3]]
        self.assertEqual(self.solution.spiral_order(matrix), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()