import unittest

class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.
        
        Args:
            s: str, input string
        Returns:
            int: Length of the longest substring without repeating characters
        
        Constraints:
            - 0 <= s.length <= 5 * 10^4
            - Target: O(n) time, O(min(m, n)) space (m is charset size)
        
        Possible Approaches:
            1. Sliding Window with Hash Set: Track characters in window
            2. Sliding Window with Hash Map: Store last seen positions
            3. Brute Force: Check all substrings (not optimal)
        """
        pass

class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "abcabcbb"
        self.assertEqual(self.solution.length_of_longest_substring(s), 3)

    def test_empty_string(self):
        s = ""
        self.assertEqual(self.solution.length_of_longest_substring(s), 0)

    def test_single_character(self):
        s = "a"
        self.assertEqual(self.solution.length_of_longest_substring(s), 1)

    def test_all_same(self):
        s = "bbbb"
        self.assertEqual(self.solution.length_of_longest_substring(s), 1)

    def test_all_unique(self):
        s = "abcde"
        self.assertEqual(self.solution.length_of_longest_substring(s), 5)

if __name__ == "__main__":
    unittest.main()