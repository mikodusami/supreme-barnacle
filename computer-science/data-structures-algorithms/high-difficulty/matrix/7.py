from typing import List
import unittest

class Solution:
    def longest_increasing_path(self, matrix: List[List[int]]) -> int:
        """
        Finds the length of the longest increasing path in a matrix.
        
        Args:
            matrix: List[List[int]], m×n matrix
        Returns:
            int: Length of longest increasing path
        
        Constraints:
            - 1 <= matrix.length, matrix[0].length <= 200
            - Target: O(m*n) time, O(m*n) space
        
        Possible Approaches:
            1. DFS with Memoization: Explore paths with caching
            2. Topological Sort: Treat as DAG with increasing edges
            3. BFS: Explore level by level (less common)
        """
        pass

class TestLongestIncreasingPath(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
        self.assertEqual(self.solution.longest_increasing_path(matrix), 4)

    def test_single_element(self):
        matrix = [[1]]
        self.assertEqual(self.solution.longest_increasing_path(matrix), 1)

    def test_all_same(self):
        matrix = [[1, 1], [1, 1]]
        self.assertEqual(self.solution.longest_increasing_path(matrix), 1)

    def test_linear_path(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(self.solution.longest_increasing_path(matrix), 3)

if __name__ == "__main__":
    unittest.main()