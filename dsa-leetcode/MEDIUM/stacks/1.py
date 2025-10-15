import unittest

class Solution:
    def is_valid(self, s: str) -> bool:
        """
        Determines if a string of parentheses is valid.
        
        Args:
            s: str, string containing '(', ')', '{', '}', '[', ']'
        Returns:
            bool: True if valid, False otherwise
        
        Constraints:
            - 1 <= s.length <= 10^4
            - s contains only '(', ')', '{', '}', '[', ']'
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Stack: Push opening brackets, pop on matching closing brackets
            2. Counter: Track balance (not suitable for order validation)
            3. Recursive Parsing: Split string recursively (complex)
        """
        pass

class TestIsValid(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "()[]{}"
        self.assertTrue(self.solution.is_valid(s))

    def test_invalid_parentheses(self):
        s = "(]"
        self.assertFalse(self.solution.is_valid(s))

    def test_empty_string(self):
        s = ""
        self.assertTrue(self.solution.is_valid(s))

    def test_nested_parentheses(self):
        s = "{[()]}"
        self.assertTrue(self.solution.is_valid(s))

if __name__ == "__main__":
    unittest.main()