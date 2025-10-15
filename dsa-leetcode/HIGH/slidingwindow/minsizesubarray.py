from typing import List
import unittest

class Solution:
    def min_subarray_len(self, target: int, nums: List[int]) -> int:
        """
        Finds the minimal length of a contiguous subarray with sum >= target.
        
        Args:
            target: int, target sum
            nums: List[int], array of positive integers
        Returns:
            int: Minimal length of subarray, or 0 if none exists
        
        Constraints:
            - 1 <= target <= 10^9
            - 1 <= nums.length <= 10^5
            - nums[i] > 0
            - Target: O(n) time, O(1) space
        
        Possible Approaches:
            1. Sliding Window: Expand window until sum >= target, then shrink
            2. Prefix Sum with Binary Search: Use prefix sums (uses extra space)
            3. Brute Force: Check all subarrays (not optimal)
        """
        pass

class TestMinSubarrayLen(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        target, nums = 7, [2, 3, 1, 2, 4, 3]
        self.assertEqual(self.solution.min_subarray_len(target, nums), 2)

    def test_no_solution(self):
        target, nums = 100, [1, 2, 3]
        self.assertEqual(self.solution.min_subarray_len(target, nums), 0)

    def test_single_element_sufficient(self):
        target, nums = 5, [5]
        self.assertEqual(self.solution.min_subarray_len(target, nums), 1)

    def test_all_elements_needed(self):
        target, nums = 6, [1, 2, 3]
        self.assertEqual(self.solution.min_subarray_len(target, nums), 3)

if __name__ == "__main__":
    unittest.main()