import unittest

class Solution:
    def longest_valid_parentheses(self, s: str) -> int:
        """
        Finds the length of the longest valid parentheses substring.
        
        Args:
            s: str, string containing only '(' and ')'
        Returns:
            int: Length of longest valid parentheses substring
        
        Constraints:
            - 0 <= s.length <= 3 * 10^4
            - s contains only '(' and ')'
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Stack: Track indices of parentheses
            2. Dynamic Programming: Track valid substring lengths
            3. Two-Pass Counter: Count left and right parentheses
        """
        pass

class TestLongestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "()(()"
        self.assertEqual(self.solution.longest_valid_parentheses(s), 2)

    def test_empty_string(self):
        s = ""
        self.assertEqual(self.solution.longest_valid_parentheses(s), 0)

    def test_valid_string(self):
        s = "(())"
        self.assertEqual(self.solution.longest_valid_parentheses(s), 4)

    def test_invalid_string(self):
        s = ")))"
        self.assertEqual(self.solution.longest_valid_parentheses(s), 0)

if __name__ == "__main__":
    unittest.main()