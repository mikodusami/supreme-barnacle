from typing import List
import unittest

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds indices of two numbers in nums that add up to target.
        
        Args:
            nums: List[int], list of integers
            target: int, target sum
        Returns:
            List[int]: Indices of the two numbers
        
        Constraints:
            - 2 <= nums.length <= 10^4
            - Each input has exactly one solution
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Hash Map: Store number-index pairs, check for complement
            2. Brute Force: Check all pairs (not optimal)
            3. Sorting + Two Pointers: Sort and use pointers (uses extra space)
        """
        pass

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums, target = [2, 7, 11, 15], 9
        self.assertEqual(sorted(self.solution.two_sum(nums, target)), [0, 1])

    def test_negative_numbers(self):
        nums, target = [-3, 4, 3, 90], 0
        self.assertEqual(sorted(self.solution.two_sum(nums, target)), [0, 2])

    def test_two_elements(self):
        nums, target = [3, 3], 6
        self.assertEqual(sorted(self.solution.two_sum(nums, target)), [0, 1])

    def test_large_numbers(self):
        nums, target = [1, 5, 10], 15
        self.assertEqual(sorted(self.solution.two_sum(nums, target)), [1, 2])

if __name__ == "__main__":
    unittest.main()