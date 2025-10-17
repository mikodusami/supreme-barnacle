from typing import List
import unittest

class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        """
        Counts the number of islands in a 2D binary grid.
        
        Args:
            grid: List[List[str]], m×n grid of '1' (land) and '0' (water)
        Returns:
            int: Number of islands
        
        Constraints:
            - 1 <= grid.length, grid[0].length <= 300
            - grid[i][j] is '0' or '1'
            - Target: O(m*n) time, O(m*n) space (or O(1) with in-place marking)
        
        Possible Approaches:
            1. DFS: Mark connected lands as visited
            2. BFS: Use queue to explore connected lands
            3. Union-Find: Group connected lands into components
        """
        pass

class TestNumberOfIslands(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        self.assertEqual(self.solution.num_islands(grid), 3)

    def test_empty_grid(self):
        grid = []
        self.assertEqual(self.solution.num_islands(grid), 0)

    def test_single_land(self):
        grid = [["1"]]
        self.assertEqual(self.solution.num_islands(grid), 1)

    def test_all_water(self):
        grid = [["0", "0"], ["0", "0"]]
        self.assertEqual(self.solution.num_islands(grid), 0)

if __name__ == "__main__":
    unittest.main()