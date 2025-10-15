from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is a valid Binary Search Tree (BST).
        
        Args:
            root: Optional[TreeNode], root of the binary tree
        Returns:
            bool: True if valid BST, False otherwise
        
        Constraints:
            - 1 <= Number of nodes <= 10^4
            - -2^31 <= Node.val <= 2^31 - 1
            - Target: O(n) time, O(h) space (n: nodes, h: tree height)
        
        Possible Approaches:
            1. Recursive DFS with Range: Check valid range for each node
            2. Inorder Traversal: Check if inorder is strictly increasing
            3. Iterative Inorder: Use stack for inorder traversal
        """
        pass

class TestIsValidBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertFalse(self.solution.is_valid_bst(root))

    def test_valid_bst(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(self.solution.is_valid_bst(root))

    def test_single_node(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.is_valid_bst(root))

    def test_empty_tree(self):
        self.assertTrue(self.solution.is_valid_bst(None))

if __name__ == "__main__":
    unittest.main()