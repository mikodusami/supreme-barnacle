import unittest

class Solution:
    def first_unique_char(self, s: str) -> int:
        """
        Finds the index of the first unique character in a string.
        
        Args:
            s: str, input string
        Returns:
            int: Index of first unique character, or -1 if none exists
        
        Constraints:
            - 0 <= s.length <= 10^5
            - Target: O(n) time, O(1) space (assuming fixed alphabet)
        
        Possible Approaches:
            1. Hash Map: Count frequencies, then find first with count 1
            2. Two Pass: Build frequency map, then scan string
            3. Brute Force: Check each character against all others (not optimal)
        """
        pass

class TestFirstUniqueChar(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "leetcode"
        self.assertEqual(self.solution.first_unique_char(s), 0)

    def test_no_unique(self):
        s = "aabb"
        self.assertEqual(self.solution.first_unique_char(s), -1)

    def test_empty_string(self):
        s = ""
        self.assertEqual(self.solution.first_unique_char(s), -1)

    def test_single_character(self):
        s = "a"
        self.assertEqual(self.solution.first_unique_char(s), 0)

if __name__ == "__main__":
    unittest.main()