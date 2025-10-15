from typing import List
import unittest

class Solution:
    def max_sum_subarray(self, nums: List[int], k: int) -> int:
        """
        Finds the maximum sum of any contiguous subarray of size k.
        
        Args:
            nums: List[int], array of positive integers
            k: int, size of the subarray
        Returns:
            int: Maximum sum of any contiguous subarray of size k
        
        Constraints:
            - 1 <= k <= nums.length <= 10^5
            - nums[i] >= 0
            - Target: O(n) time, O(1) space
        
        Possible Approaches:
            1. Sliding Window: Maintain a window of size k, update sum by adding/removing elements
            2. Prefix Sum: Compute prefix sums to calculate subarray sums (less optimal)
            3. Brute Force: Check all subarrays of size k (not optimal)
        """
        pass

class TestMaxSumSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums, k = [2, 1, 5, 1, 3, 2], 3
        self.assertEqual(self.solution.max_sum_subarray(nums, k), 9)

    def test_single_element(self):
        nums, k = [5], 1
        self.assertEqual(self.solution.max_sum_subarray(nums, k), 5)

    def test_all_same(self):
        nums, k = [3, 3, 3, 3], 2
        self.assertEqual(self.solution.max_sum_subarray(nums, k), 6)

    def test_k_equals_length(self):
        nums, k = [1, 2, 3], 3
        self.assertEqual(self.solution.max_sum_subarray(nums, k), 6)

if __name__ == "__main__":
    unittest.main()