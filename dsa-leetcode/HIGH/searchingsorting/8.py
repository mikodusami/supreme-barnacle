from typing import List
import unittest

class Solution:
    def sort_colors(self, nums: List[int]) -> None:
        """
        Sorts an array of colors (0=red, 1=white, 2=blue) in-place.
        
        Args:
            nums: List[int], array of 0s, 1s, and 2s
        Returns:
            None: Modifies nums in-place
        
        Constraints:
            - 1 <= nums.length <= 300
            - nums[i] is 0, 1, or 2
            - Target: O(n) time, O(1) space
        
        Possible Approaches:
            1. Dutch National Flag: Use three pointers to partition
            2. Counting Sort: Count occurrences, then fill array
            3. Two-Pass: Count and place elements (not optimal)
        """
        pass

class TestSortColors(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 0, 2, 1, 1, 0]
        expected = [0, 0, 1, 1, 2, 2]
        self.solution.sort_colors(nums)
        self.assertEqual(nums, expected)

    def test_single_element(self):
        nums = [1]
        expected = [1]
        self.solution.sort_colors(nums)
        self.assertEqual(nums, expected)

    def test_all_same_color(self):
        nums = [2, 2, 2]
        expected = [2, 2, 2]
        self.solution.sort_colors(nums)
        self.assertEqual(nums, expected)

    def test_sorted_colors(self):
        nums = [0, 1, 2]
        expected = [0, 1, 2]
        self.solution.sort_colors(nums)
        self.assertEqual(nums, expected)

if __name__ == "__main__":
    unittest.main()