import unittest

class Solution:
    def remove_duplicates(self, s: str) -> str:
        """
        Repeatedly removes adjacent duplicate characters from a string.
        
        Args:
            s: str, input string
        Returns:
            str: Final string after all duplicate removals
        
        Constraints:
            - 1 <= s.length <= 10^5
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Stack: Push characters, pop on duplicates
            2. Two Pointers: Simulate stack with string manipulation
            3. Recursive: Remove duplicates recursively (less efficient)
        """
        pass

class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "abbaca"
        self.assertEqual(self.solution.remove_duplicates(s), "ca")

    def test_no_duplicates(self):
        s = "abc"
        self.assertEqual(self.solution.remove_duplicates(s), "abc")

    def test_empty_string(self):
        s = ""
        self.assertEqual(self.solution.remove_duplicates(s), "")

    def test_all_duplicates(self):
        s = "aaaa"
        self.assertEqual(self.solution.remove_duplicates(s), "")

if __name__ == "__main__":
    unittest.main()