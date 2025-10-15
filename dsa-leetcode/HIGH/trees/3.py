from typing import List, Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the pre-order traversal (Root, Left, Right) of a binary tree.
        
        Args:
            root: Optional[TreeNode], root of the binary tree
        Returns:
            List[int]: List of node values in pre-order
        
        Constraints:
            - 0 <= Number of nodes <= 100
            - Target: O(n) time, O(h) space (n: nodes, h: tree height)
        
        Possible Approaches:
            1. Recursive DFS: Traverse root, left, right
            2. Iterative DFS: Use stack to simulate recursion
            3. Morris Traversal: Adapt for pre-order with O(1) space
        """
        pass

class TestPreorderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(self.solution.preorder_traversal(root), [1, 2, 3])

    def test_empty_tree(self):
        self.assertEqual(self.solution.preorder_traversal(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.preorder_traversal(root), [1])

    def test_right_skewed(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.solution.preorder_traversal(root), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()