import unittest

class MinStack:
    def __init__(self):
        """
        Initializes a stack that supports O(1) push, pop, top, and getMin.
        
        Constraints:
            - Operations should be O(1) time
            - Target: O(n) space for n elements
        """
        pass

    def push(self, val: int) -> None:
        """
        Pushes element val onto the stack.
        
        Args:
            val: int, element to push
        """
        pass

    def pop(self) -> None:
        """
        Removes the top element from the stack.
        """
        pass

    def top(self) -> int:
        """
        Returns the top element without removing it.
        
        Returns:
            int: Top element
        """
        pass

    def getMin(self) -> int:
        """
        Returns the minimum element in the stack.
        
        Returns:
            int: Minimum element
        """
        pass

class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.stack = MinStack()

    def test_example_1(self):
        self.stack.push(-2)
        self.stack.push(0)
        self.stack.push(-3)
        self.assertEqual(self.stack.getMin(), -3)
        self.stack.pop()
        self.assertEqual(self.stack.top(), 0)
        self.assertEqual(self.stack.getMin(), -2)

    def test_empty_stack(self):
        with self.assertRaises(Exception):
            self.stack.pop()
        with self.assertRaises(Exception):
            self.stack.top()
        with self.assertRaises(Exception):
            self.stack.getMin()

    def test_single_element(self):
        self.stack.push(1)
        self.assertEqual(self.stack.getMin(), 1)
        self.assertEqual(self.stack.top(), 1)

    def test_multiple_pushes(self):
        self.stack.push(3)
        self.stack.push(5)
        self.stack.push(2)
        self.stack.push(1)
        self.assertEqual(self.stack.getMin(), 1)

if __name__ == "__main__":
    unittest.main()