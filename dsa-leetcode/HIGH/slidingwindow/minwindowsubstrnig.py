import unittest

class Solution:
    def min_window(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring of s containing all characters in t (including duplicates).
        
        Args:
            s: str, input string
            t: str, target string
        Returns:
            str: Minimum window substring, or empty string if none exists
        
        Constraints:
            - 1 <= s.length, t.length <= 10^5
            - Target: O(n) time, O(1) space (assuming fixed alphabet)
        
        Possible Approaches:
            1. Sliding Window with Hash Map: Track required characters, shrink when valid
            2. Sliding Window with Array: Use array for fixed-size alphabet
            3. Brute Force: Check all substrings (not optimal)
        """
        pass

class TestMinWindow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s, t = "ADOBECODEBANC", "ABC"
        self.assertEqual(self.solution.min_window(s, t), "BANC")

    def test_no_solution(self):
        s, t = "a", "b"
        self.assertEqual(self.solution.min_window(s, t), "")

    def test_single_character(self):
        s, t = "a", "a"
        self.assertEqual(self.solution.min_window(s, t), "a")

    def test_exact_match(self):
        s, t = "abc", "abc"
        self.assertEqual(self.solution.min_window(s, t), "abc")

if __name__ == "__main__":
    unittest.main()