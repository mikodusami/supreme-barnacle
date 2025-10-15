from typing import List
import unittest

class Solution:
    def find_averages(self, nums: List[int], k: int) -> List[float]:
        """
        Finds the average of all contiguous subarrays of size k.
        
        Args:
            nums: List[int], array of integers
            k: int, size of the subarray
        Returns:
            List[float]: List of averages of all contiguous subarrays of size k
        
        Constraints:
            - 1 <= k <= nums.length <= 10^5
            - Target: O(n) time, O(1) space (excluding output)
        
        Possible Approaches:
            1. Sliding Window: Maintain a window sum, compute average for each window
            2. Prefix Sum: Use prefix sums to compute subarray sums (less optimal)
            3. Brute Force: Compute sum for each subarray (not optimal)
        """
        pass

class TestFindAverages(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums, k = [1, 12, -5, -6, 50, 3], 4
        self.assertEqual(self.solution.find_averages(nums, k), [0.5, 12.75, 12.0])

    def test_single_element(self):
        nums, k = [5], 1
        self.assertEqual(self.solution.find_averages(nums, k), [5.0])

    def test_k_equals_length(self):
        nums, k = [1, 2, 3], 3
        self.assertEqual(self.solution.find_averages(nums, k), [2.0])

    def test_negative_numbers(self):
        nums, k = [-1, -2, -3, -4], 2
        self.assertEqual(self.solution.find_averages(nums, k), [-1.5, -2.5, -3.5])

if __name__ == "__main__":
    unittest.main()