import unittest

class Solution:
    def first_bad_version(self, n: int) -> int:
        """
        Finds the first bad version among n versions using is_bad_version API.
        
        Args:
            n: int, total number of versions
        Returns:
            int: First bad version
        
        Constraints:
            - 1 <= n <= 2^31 - 1
            - Target: O(log n) time, O(1) space
        
        Possible Approaches:
            1. Binary Search: Find leftmost bad version
            2. Linear Scan: Check each version (not optimal)
            3. Recursive Binary Search: Divide range recursively
        """
        pass

class TestFirstBadVersion(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        def is_bad_version(version):
            return version >= 4
        self.solution.is_bad_version = is_bad_version
        n = 5
        self.assertEqual(self.solution.first_bad_version(n), 4)

    def test_single_version(self):
        def is_bad_version(version):
            return version >= 1
        self.solution.is_bad_version = is_bad_version
        n = 1
        self.assertEqual(self.solution.first_bad_version(n), 1)

    def test_last_version(self):
        def is_bad_version(version):
            return version >= 5
        self.solution.is_bad_version = is_bad_version
        n = 5
        self.assertEqual(self.solution.first_bad_version(n), 5)

    def test_all_bad(self):
        def is_bad_version(version):
            return version >= 1
        self.solution.is_bad_version = is_bad_version
        n = 3
        self.assertEqual(self.solution.first_bad_version(n), 1)

if __name__ == "__main__":
    unittest.main()