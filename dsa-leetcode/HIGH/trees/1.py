from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum depth of a binary tree.
        
        Args:
            root: Optional[TreeNode], root of the binary tree
        Returns:
            int: Maximum depth (longest path from root to leaf)
        
        Constraints:
            - 0 <= Number of nodes <= 10^4
            - Target: O(n) time, O(h) space (n: nodes, h: tree height)
        
        Possible Approaches:
            1. Recursive DFS: Compute max depth of left and right subtrees
            2. Iterative BFS: Use queue to count levels
            3. Iterative DFS: Use stack with depth tracking
        """
        pass

class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.max_depth(root), 3)

    def test_empty_tree(self):
        self.assertEqual(self.solution.max_depth(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.max_depth(root), 1)

    def test_skewed_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(self.solution.max_depth(root), 3)

if __name__ == "__main__":
    unittest.main()