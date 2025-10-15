from typing import List
import unittest

class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        """
        Determines if the last index can be reached starting from index 0.
        Each element represents the maximum jump length from that position.
        
        Args:
            nums: List[int], list of non-negative integers
        Returns:
            bool: True if last index is reachable, False otherwise
        
        Constraints:
            - 1 <= nums.length <= 10^4
            - 0 <= nums[i] <= 10^5
            - Target: O(n) time, O(1) space
        
        Possible Approaches:
            1. Greedy: Track maximum reachable index
            2. Dynamic Programming: Track reachable indices (uses extra space)
            3. Backtracking: Explore all jumps (not optimal)
        """
        pass

class TestCanJump(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 3, 1, 1, 4]
        self.assertTrue(self.solution.can_jump(nums))

    def test_cannot_reach(self):
        nums = [3, 2, 1, 0, 4]
        self.assertFalse(self.solution.can_jump(nums))

    def test_single_element(self):
        nums = [0]
        self.assertTrue(self.solution.can_jump(nums))

    def test_two_elements(self):
        nums = [1, 0]
        self.assertTrue(self.solution.can_jump(nums))

    def test_all_zeros_except_first(self):
        nums = [1, 0, 0]
        self.assertFalse(self.solution.can_jump(nums))

if __name__ == "__main__":
    unittest.main()