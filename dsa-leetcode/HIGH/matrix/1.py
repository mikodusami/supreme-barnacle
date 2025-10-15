from typing import List
import unittest

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Returns the transpose of an m×n matrix by flipping it over its main diagonal.
        
        Args:
            matrix: List[List[int]], m×n matrix
        Returns:
            List[List[int]]: Transposed n×m matrix
        
        Constraints:
            - 1 <= matrix.length, matrix[0].length <= 1000
            - Target: O(m*n) time, O(m*n) space
        
        Possible Approaches:
            1. Create New Matrix: Build n×m matrix by swapping indices
            2. In-Place (Square Matrix): Swap elements across diagonal (not applicable for non-square)
            3. Brute Force: Iterate and fill new matrix
        """
        pass

class TestTranspose(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(self.solution.transpose(matrix), [[1, 4], [2, 5], [3, 6]])

    def test_square_matrix(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(self.solution.transpose(matrix), [[1, 3], [2, 4]])

    def test_single_element(self):
        matrix = [[1]]
        self.assertEqual(self.solution.transpose(matrix), [[1]])

    def test_single_row(self):
        matrix = [[1, 2, 3]]
        self.assertEqual(self.solution.transpose(matrix), [[1], [2], [3]])

if __name__ == "__main__":
    unittest.main()