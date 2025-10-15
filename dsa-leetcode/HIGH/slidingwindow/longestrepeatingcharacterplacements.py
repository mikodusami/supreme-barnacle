import unittest

class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        """
        Finds the longest substring with all repeating letters after at most k replacements.
        
        Args:
            s: str, input string of uppercase letters
            k: int, maximum number of replacements
        Returns:
            int: Length of the longest valid substring
        
        Constraints:
            - 1 <= s.length <= 10^5
            - 0 <= k <= s.length
            - Target: O(n) time, O(1) space (assuming fixed alphabet)
        
        Possible Approaches:
            1. Sliding Window: Track most frequent character, shrink if replacements exceed k
            2. Binary Search: Check if a length is feasible (less practical)
            3. Brute Force: Try all substrings (not optimal)
        """
        pass

class TestCharacterReplacement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s, k = "AABABBA", 1
        self.assertEqual(self.solution.character_replacement(s, k), 4)

    def test_k_zero(self):
        s, k = "ABAB", 0
        self.assertEqual(self.solution.character_replacement(s, k), 2)

    def test_single_character(self):
        s, k = "A", 0
        self.assertEqual(self.solution.character_replacement(s, k), 1)

    def test_all_same(self):
        s, k = "AAAA", 2
        self.assertEqual(self.solution.character_replacement(s, k), 4)

if __name__ == "__main__":
    unittest.main()