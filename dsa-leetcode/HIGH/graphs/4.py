from typing import Optional
import unittest

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def clone_graph(self, node: Optional[Node]) -> Optional[Node]:
        """
        Returns a deep copy of a connected undirected graph.
        
        Args:
            node: Optional[Node], reference to a node in the graph
        Returns:
            Optional[Node]: Reference to the cloned graph's starting node
        
        Constraints:
            - 1 <= Number of nodes <= 100
            - Graph is connected and undirected
            - Target: O(V + E) time, O(V) space (V: vertices, E: edges)
        
        Possible Approaches:
            1. DFS: Recursively clone nodes and neighbors
            2. BFS: Use queue to clone nodes level by level
            3. Iterative with Hash Map: Map original to cloned nodes
        """
        pass

class TestCloneGraph(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Create graph: 1<->2, 1<->4, 2<->3, 3<->4
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]
        cloned = self.solution.clone_graph(node1)
        self.assertIsNotNone(cloned)
        self.assertNotEqual(cloned, node1)
        self.assertEqual(cloned.val, 1)
        self.assertEqual(len(cloned.neighbors), 2)

    def test_single_node(self):
        node = Node(1)
        cloned = self.solution.clone_graph(node)
        self.assertIsNotNone(cloned)
        self.assertNotEqual(cloned, node)
        self.assertEqual(cloned.val, 1)
        self.assertEqual(cloned.neighbors, [])

    def test_empty_graph(self):
        self.assertIsNone(self.solution.clone_graph(None))

if __name__ == "__main__":
    unittest.main()