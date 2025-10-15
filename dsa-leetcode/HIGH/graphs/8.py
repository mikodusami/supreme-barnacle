from typing import List, Dict
import unittest

class Solution:
    def dijkstra(self, n: int, edges: List[tuple[int, int, int]], src: int) -> Dict[int, int]:
        """
        Finds the shortest distance from src to all other nodes in a weighted directed graph.
        
        Args:
            n: int, number of nodes (0 to n-1)
            edges: List[tuple[int, int, int]], list of (from, to, weight)
            src: int, source node
        Returns:
            Dict[int, int]: Map of nodes to their shortest distance from src
        
        Constraints:
            - 1 <= n <= 100
            - 0 <= edges.length <= 1000
            - Target: O(E log V) time, O(V) space (V: vertices, E: edges)
        
        Possible Approaches:
            1. Dijkstra with Min-Heap: Use priority queue for shortest paths
            2. Dijkstra with Array: Use array for small graphs (less efficient)
            3. Bellman-Ford: Handle negative weights (not needed here)
        """
        pass

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n, edges, src = 5, [(0, 1, 10), (0, 2, 5), (1, 3, 1), (2, 1, 3), (2, 3, 9), (2, 4, 2), (3, 4, 4), (4, 3, 6), (4, 0, 7)], 0
        self.assertEqual(self.solution.dijkstra(n, edges, src), {0: 0, 1: 8, 2: 5, 3: 9, 4: 7})

    def test_single_node(self):
        n, edges, src = 1, [], 0
        self.assertEqual(self.solution.dijkstra(n, edges, src), {0: 0})

    def test_no_edges(self):
        n, edges, src = 3, [], 0
        self.assertEqual(self.solution.dijkstra(n, edges, src), {0: 0, 1: float('inf'), 2: float('inf')})

    def test_linear_graph(self):
        n, edges, src = 3, [(0, 1, 1), (1, 2, 1)], 0
        self.assertEqual(self.solution.dijkstra(n, edges, src), {0: 0, 1: 1, 2: 2})

if __name__ == "__main__":
    unittest.main()