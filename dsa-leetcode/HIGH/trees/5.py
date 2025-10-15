from typing import List, Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Returns the level order traversal of a binary tree.
        
        Args:
            root: Optional[TreeNode], root of the binary tree
        Returns:
            List[List[int]]: List of lists, each containing node values at a level
        
        Constraints:
            - 0 <= Number of nodes <= 2000
            - Target: O(n) time, O(w) space (n: nodes, w: max width)
        
        Possible Approaches:
            1. BFS with Queue: Process nodes level by level
            2. Recursive DFS: Track levels in recursion
            3. Iterative with Two Queues: Separate current and next level
        """
        pass

class TestLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.level_order(root), [[3], [9, 20], [15, 7]])

    def test_empty_tree(self):
        self.assertEqual(self.solution.level_order(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.level_order(root), [[1]])

    def test_linear_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(self.solution.level_order(root), [[1], [2], [3]])

if __name__ == "__main__":
    unittest.main()