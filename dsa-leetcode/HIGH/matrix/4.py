from typing import List
import unittest

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates an n×n matrix 90 degrees clockwise in-place.
        
        Args:
            matrix: List[List[int]], n×n matrix
        Returns:
            None: Modifies matrix in-place
        
        Constraints:
            - matrix.length == matrix[0].length
            - 1 <= matrix.length <= 20
            - Target: O(n^2) time, O(1) space
        
        Possible Approaches:
            1. Transpose and Reverse: Transpose matrix, then reverse each row
            2. Four-Way Swap: Rotate groups of four cells
            3. Temporary Matrix: Use extra space (not optimal)
        """
        pass

class TestRotate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_1x1_matrix(self):
        matrix = [[1]]
        expected = [[1]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_2x2_matrix(self):
        matrix = [[1, 2], [3, 4]]
        expected = [[3, 1], [4, 2]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_4x4_matrix(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expected = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

if __name__ == "__main__":
    unittest.main()