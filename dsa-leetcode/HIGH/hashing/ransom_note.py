import unittest

class Solution:
    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        """
        Checks if ransomNote can be constructed from magazine.
        
        Args:
            ransomNote: str, string to construct
            magazine: str, string providing characters
        Returns:
            bool: True if ransomNote can be constructed, False otherwise
        
        Constraints:
            - 1 <= ransomNote.length, magazine.length <= 10^5
            - Target: O(n) time, O(1) space (assuming fixed alphabet)
        
        Possible Approaches:
            1. Hash Map: Count characters in magazine, check against ransomNote
            2. Array Count: Use array for fixed-size alphabet
            3. Brute Force: Search each character (not optimal)
        """
        pass

class TestCanConstruct(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        ransomNote, magazine = "aa", "aab"
        self.assertTrue(self.solution.can_construct(ransomNote, magazine))

    def test_cannot_construct(self):
        ransomNote, magazine = "aa", "ab"
        self.assertFalse(self.solution.can_construct(ransomNote, magazine))

    def test_empty_ransomNote(self):
        ransomNote, magazine = "", "abc"
        self.assertTrue(self.solution.can_construct(ransomNote, magazine))

    def test_single_character(self):
        ransomNote, magazine = "a", "a"
        self.assertTrue(self.solution.can_construct(ransomNote, magazine))

if __name__ == "__main__":
    unittest.main()