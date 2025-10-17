from typing import List
import unittest

class Solution:
    def find_center(self, edges: List[List[int]]) -> int:
        """
        Finds the center node of a star graph given its edges.
        
        Args:
            edges: List[List[int]], list of edges [u, v]
        Returns:
            int: Value of the center node
        
        Constraints:
            - 3 <= edges.length <= 10^5
            - Graph is a valid star graph
            - Target: O(1) time, O(1) space
        
        Possible Approaches:
            1. Check First Two Edges: Center node appears in both
            2. Degree Count: Node with degree n-1 is center (uses extra space)
            3. Adjacency List: Build graph and find center (not optimal)
        """
        pass

class TestFindCenter(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        edges = [[1, 2], [2, 3], [4, 2]]
        self.assertEqual(self.solution.find_center(edges), 2)

    def test_minimum_star(self):
        edges = [[1, 2], [2, 3]]
        self.assertEqual(self.solution.find_center(edges), 2)

    def test_large_star(self):
        edges = [[1, 2], [2, 3], [2, 4], [2, 5]]
        self.assertEqual(self.solution.find_center(edges), 2)

if __name__ == "__main__":
    unittest.main()