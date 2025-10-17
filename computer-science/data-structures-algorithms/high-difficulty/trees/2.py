from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree by swapping left and right children of each node.
        
        Args:
            root: Optional[TreeNode], root of the binary tree
        Returns:
            Optional[TreeNode]: Root of the inverted tree
        
        Constraints:
            - 0 <= Number of nodes <= 100
            - Target: O(n) time, O(h) space (n: nodes, h: tree height)
        
        Possible Approaches:
            1. Recursive DFS: Swap children recursively
            2. Iterative BFS: Use queue to swap children level by level
            3. Iterative DFS: Use stack to swap children
        """
        pass

class TestInvertTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        inverted = self.solution.invert_tree(root)
        self.assertEqual(self.inorder_traversal(inverted), [9, 7, 6, 4, 3, 2, 1])

    def test_empty_tree(self):
        self.assertIsNone(self.solution.invert_tree(None))

    def test_single_node(self):
        root = TreeNode(1)
        inverted = self.solution.invert_tree(root)
        self.assertEqual(inverted.val, 1)
        self.assertIsNone(inverted.left)
        self.assertIsNone(inverted.right)

    def test_two_nodes(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        inverted = self.solution.invert_tree(root)
        self.assertEqual(self.inorder_traversal(inverted), [1, 2])

    def inorder_traversal(self, root):
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result

if __name__ == "__main__":
    unittest.main()