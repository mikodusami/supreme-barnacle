from typing import Optional, List
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs a binary tree from preorder and inorder traversals.
        
        Args:
            preorder: List[int], pre-order traversal
            inorder: List[int], in-order traversal
        Returns:
            Optional[TreeNode]: Root of the constructed tree
        
        Constraints:
            - 1 <= preorder.length == inorder.length <= 100
            - No duplicate values
            - Target: O(n) time, O(n) space (n: nodes)
        
        Possible Approaches:
            1. Recursive: Use preorder for root, inorder for subtrees
            2. Iterative: Use stack to build tree
            3. Hash Map: Map inorder values to indices for faster lookup
        """
        pass

class TestBuildTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        root = self.solution.build_tree(preorder, inorder)
        self.assertEqual(self.inorder_traversal(root), [9, 3, 15, 20, 7])
        self.assertEqual(self.preorder_traversal(root), [3, 9, 20, 15, 7])

    def test_single_node(self):
        preorder = [1]
        inorder = [1]
        root = self.solution.build_tree(preorder, inorder)
        self.assertEqual(self.inorder_traversal(root), [1])

    def test_left_skewed(self):
        preorder = [1, 2, 3]
        inorder = [3, 2, 1]
        root = self.solution.build_tree(preorder, inorder)
        self.assertEqual(self.inorder_traversal(root), [3, 2, 1])

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

    def preorder_traversal(self, root):
        result = []
        def dfs(node):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result

if __name__ == "__main__":
    unittest.main()