from typing import List
import unittest

class Solution:
    def num_subarray_product_less_than_k(self, nums: List[int], k: int) -> int:
        """
        Counts the number of contiguous subarrays with product less than k.
        
        Args:
            nums: List[int], array of positive integers
            k: int, target product threshold
        Returns:
            int: Number of valid subarrays
        
        Constraints:
            - 1 <= nums.length <= 3 * 10^4
            - nums[i] > 0
            - k >= 0
            - Target: O(n) time, O(1) space
        
        Possible Approaches:
            1. Sliding Window: Maintain product in window, count valid subarrays
            2. Brute Force: Check all subarrays (not optimal)
            3. Prefix Product: Use product prefixes (less practical)
        """
        pass

class TestNumSubarrayProductLessThanK(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums, k = [10, 5, 2, 6], 100
        self.assertEqual(self.solution.num_subarray_product_less_than_k(nums, k), 8)

    def test_k_zero(self):
        nums, k = [1, 2, 3], 0
        self.assertEqual(self.solution.num_subarray_product_less_than_k(nums, k), 0)

    def test_single_element(self):
        nums, k = [5], 10
        self.assertEqual(self.solution.num_subarray_product_less_than_k(nums, k), 1)

    def test_all_large(self):
        nums, k = [10, 10, 10], 5
        self.assertEqual(self.solution.num_subarray_product_less_than_k(nums, k), 0)

if __name__ == "__main__":
    unittest.main()