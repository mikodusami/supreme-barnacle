"""
Binary Trees Study Guide and Code Template

This file serves as a comprehensive resource for mastering the Binary Tree data structure,
including core implementation, common interview traversals and patterns, and auxiliary utilities.
"""

from typing import Any, List, Optional, TypeVar, Generic, Deque, Callable, Tuple
from collections import deque
# Type variable for generics
T = TypeVar('T')
# =============================================================================
# I. Core Implementation & Theory (The Foundation)
# =============================================================================
class TreeNode(Generic[T]):
    """
    Core structure for a Binary Tree Node.
    """
    def __init__(self, val: T = None):
        super().__init__()
        self.val: T = val
        self.left: Optional['TreeNode[T]'] = None
        self.right: Optional['TreeNode[T]'] = None

# --- Core Traversal Implementations ---
class BinaryTreeTraversal:
    """
    Standard traversal algorithms for a Binary Tree.

    Time Complexity for all traversals (iterative and recursive):
        O(N), where N is the number of nodes, as each node is visited exactly once.
    Space Complexity for all traversals:
        O(H) where H is the height of the tree, due to recursion stack depth (recursive)
        or explicit stack/queue storage (iterative). H can be O(log N) for balanced trees
        or O(N) for skewed trees.
    """
    
    # pre order: ROOT, LEFT, RIGHT
    # in order; LEFT, ROOT, RIGHT
    # post order: LEFT, RIGHT, ROOT
    def preorder_recursive(root: Optional[TreeNode[T]]) -> List[T]:
        # ROOT, LEFT, RIGHT
        result = []
        def traverse(node):
            if node:
                result.append(node.val)
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return result
    
    def postorder_recursive(root: Optional[TreeNode[T]]) -> List[T]:
        result = []
        # Node -> Left, Right, Root
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.val)
        traverse(root)
        return result