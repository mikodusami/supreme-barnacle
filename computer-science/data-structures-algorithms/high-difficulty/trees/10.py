from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Serializes a binary tree to a string.
        
        Args:
            root: Optional[TreeNode], root of the binary tree
        Returns:
            str: String representation of the tree
        
        Constraints:
            - 0 <= Number of nodes <= 10^4
            - Target: O(n) time, O(n) space (n: nodes)
        
        Possible Approaches:
            1. Pre-order DFS: Serialize using pre-order traversal
            2. Level-order BFS: Serialize level by level
            3. Post-order DFS: Use post-order traversal
        """
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Deserializes a string to a binary tree.
        
        Args:
            data: str, string representation of the tree
        Returns:
            Optional[TreeNode]: Root of the reconstructed tree
        
        Constraints:
            - Input string is valid (from serialize)
            - Target: O(n) time, O(n) space (n: nodes)
        
        Possible Approaches:
            1. Pre-order DFS: Reconstruct using pre-order traversal
            2. Level-order BFS: Reconstruct level by level
            3. Post-order DFS: Reconstruct using post-order traversal
        """
        pass

class TestSerializeDeserialize(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        serialized = self.solution.serialize(root)
        deserialized = self.solution.deserialize(serialized)
        self.assertEqual(self.preorder_traversal(deserialized), [1, 2, 3, 4, 5])

    def test_empty_tree(self):
        serialized = self.solution.serialize(None)
        deserialized = self.solution.deserialize(serialized)
        self.assertIsNone(deserialized)

    def test_single_node(self):
        root = TreeNode(1)
        serialized = self.solution.serialize(root)
        deserialized = self.solution.deserialize(serialized)
        self.assertEqual(self.preorder_traversal(deserialized), [1])

    def test_linear_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        serialized = self.solution.serialize(root)
        deserialized = self.solution.deserialize(serialized)
        self.assertEqual(self.preorder_traversal(deserialized), [1, 2, 3])

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