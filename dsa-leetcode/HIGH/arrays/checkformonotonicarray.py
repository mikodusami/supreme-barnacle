from typing import List
import unittest

class Solution:
    def is_monotonic(self, nums: List[int]) -> bool:
        """
        Determines if a list is monotonic (non-decreasing or non-increasing).
        Empty lists and single-element lists are considered monotonic.
        
        Args:
            nums: List[int], list of integers
        Returns:
            bool: True if the list is monotonic, False otherwise
        
        Constraints:
            - 0 <= nums.length <= 10^5
            - Target: O(n) time, O(1) space
        """
        pass

class TestIsMonotonic(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 2, 3]
        self.assertTrue(self.solution.is_monotonic(nums))

    def test_empty_list(self):
        nums = []
        self.assertTrue(self.solution.is_monotonic(nums))

    def test_single_element(self):
        nums = [1]
        self.assertTrue(self.solution.is_monotonic(nums))

    def test_non_increasing(self):
        nums = [3, 2, 2, 1]
        self.assertTrue(self.solution.is_monotonic(nums))

    def test_non_monotonic(self):
        nums = [1, 3, 2]
        self.assertFalse(self.solution.is_monotonic(nums))

    def test_same_elements(self):
        nums = [2, 2, 2, 2]
        self.assertTrue(self.solution.is_monotonic(nums))

if __name__ == "__main__":
    unittest.main()