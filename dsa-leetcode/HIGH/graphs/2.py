from typing import List, Dict
import unittest

class Solution:
    def dfs_traversal(self, graph: Dict[int, List[int]], start_node: int) -> List[int]:
        """
        Returns a list of nodes visited in DFS order starting from start_node.
        
        Args:
            graph: Dict[int, List[int]], adjacency list of undirected graph
            start_node: int, starting node for DFS
        Returns:
            List[int]: Nodes in DFS order
        
        Constraints:
            - Graph is undirected, nodes are integers
            - start_node exists in graph
            - Target: O(V + E) time, O(V) space (V: vertices, E: edges)
        
        Possible Approaches:
            1. Recursive DFS: Use recursion to explore neighbors
            2. Iterative DFS: Use a stack to explore nodes
            3. Backtracking: Explore all paths recursively
        """
        pass

class TestDFSTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        graph = {1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}
        start_node = 1
        self.assertEqual(self.solution.dfs_traversal(graph, start_node), [1, 2, 4, 3, 5])

    def test_single_node(self):
        graph = {1: []}
        start_node = 1
        self.assertEqual(self.solution.dfs_traversal(graph, start_node), [1])

    def test_disconnected_nodes(self):
        graph = {1: [2], 2: [1], 3: []}
        start_node = 1
        self.assertEqual(self.solution.dfs_traversal(graph, start_node), [1, 2])

    def test_complete_graph(self):
        graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
        start_node = 1
        self.assertEqual(sorted(self.solution.dfs_traversal(graph, start_node)), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()