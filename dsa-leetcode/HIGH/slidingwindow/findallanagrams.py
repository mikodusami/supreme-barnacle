from typing import List
import unittest

class Solution:
    def find_anagrams(self, s: str, p: str) -> List[int]:
        """
        Finds all starting indices of p's anagrams in s.
        
        Args:
            s: str, input string
            p: str, pattern string
        Returns:
            List[int]: List of starting indices of anagrams
        
        Constraints:
            - 1 <= s.length, p.length <= 3 * 10^4
            - Target: O(n) time, O(1) space (assuming fixed alphabet)
        
        Possible Approaches:
            1. Sliding Window with Hash Map: Compare character frequencies
            2. Sliding Window with Array: Use array for fixed-size alphabet
            3. Brute Force: Check each substring (not optimal)
        """
        pass

class TestFindAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s, p = "cbaebabacd", "abc"
        self.assertEqual(self.solution.find_anagrams(s, p), [0, 6])

    def test_no_anagrams(self):
        s, p = "xyz", "abc"
        self.assertEqual(self.solution.find_anagrams(s, p), [])

    def test_single_character(self):
        s, p = "aaa", "a"
        self.assertEqual(self.solution.find_anagrams(s, p), [0, 1, 2])

    def test_same_string(self):
        s, p = "abc", "abc"
        self.assertEqual(self.solution.find_anagrams(s, p), [0])

if __name__ == "__main__":
    unittest.main()