from typing import List, Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def path_sum(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
        """
        Finds all root-to-leaf paths where the sum of node values equals target_sum.
        
        Args:
            root: Optional[TreeNode], root of the binary tree
            target_sum: int, target sum for paths
        Returns:
            List[List[int]]: List of paths (as lists of node values)
        
        Constraints:
            - 0 <= Number of nodes <= 5000
            - -1000 <= Node.val, target_sum <= 1000
            - Target: O(n) time, O(h) space (n: nodes, h: tree height)
        
        Possible Approaches:
            1. Recursive DFS: Track path and sum, add valid paths
            2. Iterative DFS: Use stack to track paths and sums
            3. Backtracking: Build paths and backtrack on exploration
        """
        pass

class TestPathSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        target_sum = 22
        self.assertEqual(sorted(self.solution.path_sum(root, target_sum)), sorted([[5, 4, 11, 2], [5, 8, 4, 5]]))

    def test_empty_tree(self):
        self.assertEqual(self.solution.path_sum(None, 0), [])

    def test_single_node(self):
        root = TreeNode(1)
        target_sum = 1
        self.assertEqual(self.solution.path_sum(root, target_sum), [[1]])

    def test_no_valid_path(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        target_sum = 5
        self.assertEqual(self.solution.path_sum(root, target_sum), [])

if __name__ == "__main__":
    unittest.main()