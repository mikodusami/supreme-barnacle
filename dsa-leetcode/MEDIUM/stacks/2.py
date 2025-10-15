import unittest

class ArrayStack:
    def __init__(self):
        """
        Initializes an empty stack.
        
        Constraints:
            - Stack operations should be O(1) time
            - Target: O(n) space for n elements
        """
        pass

    def push(self, x: int) -> None:
        """
        Pushes element x onto the stack.
        
        Args:
            x: int, element to push
        """
        pass

    def pop(self) -> int:
        """
        Removes and returns the top element of the stack.
        
        Returns:
            int: Top element
        """
        pass

    def top(self) -> int:
        """
        Returns the top element without removing it.
        
        Returns:
            int: Top element
        """
        pass

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.
        
        Returns:
            bool: True if empty, False otherwise
        """
        pass

class TestArrayStack(unittest.TestCase):
    def setUp(self):
        self.stack = ArrayStack()

    def test_example_1(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.top(), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertFalse(self.stack.is_empty())

    def test_empty_stack(self):
        self.assertTrue(self.stack.is_empty())
        with self.assertRaises(Exception):
            self.stack.pop()
        with self.assertRaises(Exception):
            self.stack.top()

    def test_single_element(self):
        self.stack.push(1)
        self.assertEqual(self.stack.top(), 1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())

    def test_multiple_pushes_pops(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.top(), 1)

if __name__ == "__main__":
    unittest.main()