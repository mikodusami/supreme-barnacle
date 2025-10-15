import unittest

class Solution:
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring with at most k distinct characters.
        
        Args:
            s: str, input string
            k: int, maximum number of distinct characters
        Returns:
            int: Length of longest valid substring
        
        Constraints:
            - 1 <= s.length <= 10^5
            - 0 <= k <= s.length
            - Target: O(n) time, O(k) space
        
        Possible Approaches:
            1. Sliding Window with Hash Map: Track character counts, shrink when exceeding k
            2. Sliding Window with Ordered Dict: Track order of characters
            3. Brute Force: Check all substrings (not optimal)
        """
        pass

class TestLengthOfLongestSubstringKDistinct(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s, k = "eceba", 2
        self.assertEqual(self.solution.length_of_longest_substring_k_distinct(s, k), 3)

    def test_k_zero(self):
        s, k = "abc", 0
        self.assertEqual(self.solution.length_of_longest_substring_k_distinct(s, k), 0)

    def test_single_character(self):
        s, k = "a", 1
        self.assertEqual(self.solution.length_of_longest_substring_k_distinct(s, k), 1)

    def test_all_same(self):
        s, k = "aaa", 1
        self.assertEqual(self.solution.length_of_longest_substring_k_distinct(s, k), 3)

if __name__ == "__main__":
    unittest.main()