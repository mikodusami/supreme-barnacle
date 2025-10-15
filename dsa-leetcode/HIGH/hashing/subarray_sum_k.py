from typing import List
import unittest

class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> int:
        """
        Counts the number of contiguous subarrays with sum equal to k.
        
        Args:
            nums: List[int], array of integers
            k: int, target sum
        Returns:
            int: Number of subarrays with sum k
        
        Constraints:
            - 1 <= nums.length <= 2 * 10^4
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Prefix Sum with Hash Map: Track prefix sums, count occurrences
            2. Brute Force: Check all subarrays (not optimal)
            3. Sliding Window: Only works for non-negative numbers
        """
        pass

class TestSubarraySum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums, k = [1, 1, 1], 2
        self.assertEqual(self.solution.subarray_sum(nums, k), 2)

    def test_no_subarray(self):
        nums, k = [1, 2, 3], 10
        self.assertEqual(self.solution.subarray_sum(nums, k), 0)

    def test_single_element(self):
        nums, k = [5], 5
        self.assertEqual(self.solution.subarray_sum(nums, k), 1)

    def test_negative_numbers(self):
        nums, k = [-1, -1, 1], 0
        self.assertEqual(self.solution.subarray_sum(nums, k), 1)

if __name__ == "__main__":
    unittest.main()