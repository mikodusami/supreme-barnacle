from typing import List, Dict
import unittest

class Solution:
    def bfs_traversal(self, graph: Dict[int, List[int]], start_node: int) -> List[int]:
        """
        Returns a list of nodes visited in BFS order starting from start_node.
        
        Args:
            graph: Dict[int, List[int]], adjacency list of undirected graph
            start_node: int, starting node for BFS
        Returns:
            List[int]: Nodes in BFS order
        
        Constraints:
            - Graph is undirected, nodes are integers
            - start_node exists in graph
            - Target: O(V + E) time, O(V) space (V: vertices, E: edges)
        
        Possible Approaches:
            1. BFS with Queue: Use a queue to explore nodes level by level
            2. Iterative with Set: Track visited nodes and explore neighbors
            3. Recursive BFS: Less common, but possible with a queue
        """
        pass

class TestBFSTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        graph = {1: [2, 3], 2: [1, 4], 3: [1, 5], 4: [2], 5: [3]}
        start_node = 1
        self.assertEqual(self.solution.bfs_traversal(graph, start_node), [1, 2, 3, 4, 5])

    def test_single_node(self):
        graph = {1: []}
        start_node = 1
        self.assertEqual(self.solution.bfs_traversal(graph, start_node), [1])

    def test_disconnected_nodes(self):
        graph = {1: [2], 2: [1], 3: []}
        start_node = 1
        self.assertEqual(self.solution.bfs_traversal(graph, start_node), [1, 2])

    def test_complete_graph(self):
        graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
        start_node = 1
        self.assertEqual(sorted(self.solution.bfs_traversal(graph, start_node)), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()