from typing import List
import unittest

class Solution:
    def topological_sort(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Returns a topological ordering of nodes in a directed acyclic graph (DAG).
        
        Args:
            n: int, number of nodes (0 to n-1)
            edges: List[List[int]], list of directed edges [from, to]
        Returns:
            List[int]: A valid topological ordering
        
        Constraints:
            - 1 <= n <= 10^5
            - 0 <= edges.length <= 3 * 10^5
            - Target: O(V + E) time, O(V) space (V: vertices, E: edges)
        
        Possible Approaches:
            1. Kahn's Algorithm: Use in-degree and BFS
            2. DFS: Post-order traversal to build ordering
            3. Recursive with Stack: Similar to DFS
        """
        pass

class TestTopologicalSort(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n, edges = 4, [[1, 0], [2, 0], [3, 1], [3, 2]]
        result = self.solution.topological_sort(n, edges)
        self.assertEqual(result, [0, 1, 2, 3])

    def test_single_node(self):
        n, edges = 1, []
        self.assertEqual(self.solution.topological_sort(n, edges), [0])

    def test_no_edges(self):
        n, edges = 3, []
        self.assertEqual(sorted(self.solution.topological_sort(n, edges)), [0, 1, 2])

    def test_linear_graph(self):
        n, edges = 3, [[0, 1], [1, 2]]
        self.assertEqual(self.solution.topological_sort(n, edges), [0, 1, 2])

if __name__ == "__main__":
    unittest.main()