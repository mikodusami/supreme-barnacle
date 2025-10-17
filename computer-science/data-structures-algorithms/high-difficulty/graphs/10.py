from typing import List
import unittest

class Solution:
    def min_cost_mst_prim(self, n: int, edges: List[List[int]]) -> int:
        """
        Finds the total weight of a Minimum Spanning Tree using Prim's Algorithm.
        
        Args:
            n: int, number of nodes (0 to n-1)
            edges: List[List[int]], list of [u, v, weight] for undirected edges
        Returns:
            int: Total weight of the MST
        
        Constraints:
            - 1 <= n <= 500
            - Graph is connected and undirected
            - Target: O(E log V) time, O(V) space (V: vertices, E: edges)
        
        Possible Approaches:
            1. Prim's with Min-Heap: Select minimum weight edges
            2. Kruskal's Algorithm: Sort edges and use Union-Find (alternative)
            3. Brute Force: Check all possible spanning trees (not optimal)
        """
        pass

class TestMinCostMSTPrim(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n, edges = 4, [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
        self.assertEqual(self.solution.min_cost_mst_prim(n, edges), 15)

    def test_single_edge(self):
        n, edges = 2, [[0, 1, 1]]
        self.assertEqual(self.solution.min_cost_mst_prim(n, edges), 1)

    def test_complete_graph(self):
        n, edges = 3, [[0, 1, 1], [0, 2, 2], [1, 2, 3]]
        self.assertEqual(self.solution.min_cost_mst_prim(n, edges), 3)

    def test_linear_graph(self):
        n, edges = 3, [[0, 1, 1], [1, 2, 2]]
        self.assertEqual(self.solution.min_cost_mst_prim(n, edges), 3)

if __name__ == "__main__":
    unittest.main()