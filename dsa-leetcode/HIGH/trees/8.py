from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def count_nodes(self, root: Optional[TreeNode]) -> int:
        """
        Counts the number of nodes in a complete binary tree.
        
        Args:
            root: Optional[TreeNode], root of the complete binary tree
        Returns:
            int: Number of nodes
        
        Constraints:
            - 0 <= Number of nodes <= 5 * 10^4
            - Target: O(log^2 n) time, O(1) space (n: nodes)
        
        Possible Approaches:
            1. Height-Based: Use complete tree property to optimize counting
            2. Recursive DFS: Count nodes in left and right subtrees
            3. Iterative BFS: Use queue to count all nodes
        """
        pass

class TestCountNodes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        self.assertEqual(self.solution.count_nodes(root), 6)

    def test_empty_tree(self):
        self.assertEqual(self.solution.count_nodes(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.count_nodes(root), 1)

    def test_full_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.count_nodes(root), 3)

if __name__ == "__main__":
    unittest.main()