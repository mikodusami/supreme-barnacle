from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Finds the lowest common ancestor of two nodes in a Binary Search Tree.
        
        Args:
            root: TreeNode, root of the BST
            p: TreeNode, first node
            q: TreeNode, second node
        Returns:
            TreeNode: Lowest common ancestor node
        
        Constraints:
            - 2 <= Number of nodes <= 10^5
            - p and q exist in the tree
            - Target: O(h) time, O(1) space (h: tree height)
        
        Possible Approaches:
            1. Iterative BST Search: Use BST property to navigate
            2. Recursive BST Search: Recursively traverse based on values
            3. General Tree LCA: Find paths and compare (not optimal for BST)
        """
        pass

class TestLowestCommonAncestor(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        p, q = root.left, root.right  # Nodes with values 2 and 8
        lca = self.solution.lowest_common_ancestor(root, p, q)
        self.assertEqual(lca.val, 6)

    def test_same_node(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        p = q = root.left
        lca = self.solution.lowest_common_ancestor(root, p, q)
        self.assertEqual(lca.val, 1)

    def test_parent_child(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        p, q = root, root.left
        lca = self.solution.lowest_common_ancestor(root, p, q)
        self.assertEqual(lca.val, 2)

if __name__ == "__main__":
    unittest.main()