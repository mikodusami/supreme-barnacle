from typing import List
import unittest

class Solution:
    def longest_ones(self, nums: List[int], k: int) -> int:
        """
        Finds the maximum number of consecutive 1's if you can flip at most k zeros.
        
        Args:
            nums: List[int], binary array of 0's and 1's
            k: int, maximum number of zeros that can be flipped
        Returns:
            int: Maximum number of consecutive 1's after flipping
        
        Constraints:
            - 1 <= nums.length <= 10^5
            - nums[i] is 0 or 1
            - 0 <= k <= nums.length
            - Target: O(n) time, O(1) space
        
        Possible Approaches:
            1. Sliding Window: Track zeros in window, shrink when exceeding k
            2. Brute Force: Try all possible windows (not optimal)
            3. Prefix Sum: Track zeros in ranges (less practical)
        """
        pass

class TestLongestOnes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums, k = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2
        self.assertEqual(self.solution.longest_ones(nums, k), 6)

    def test_no_zeros(self):
        nums, k = [1, 1, 1], 0
        self.assertEqual(self.solution.longest_ones(nums, k), 3)

    def test_all_zeros(self):
        nums, k = [0, 0, 0], 2
        self.assertEqual(self.solution.longest_ones(nums, k), 2)

    def test_k_zero(self):
        nums, k = [1, 0, 1, 0], 0
        self.assertEqual(self.solution.longest_ones(nums, k), 1)

if __name__ == "__main__":
    unittest.main()