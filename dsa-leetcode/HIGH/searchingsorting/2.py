from typing import List
import unittest

class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a sorted array.
        
        Args:
            nums: List[int], sorted array of integers
            target: int, value to find
        Returns:
            int: Index of target, or -1 if not found
        
        Constraints:
            - 1 <= nums.length <= 10^4
            - nums is sorted in ascending order
            - Target: O(log n) time, O(1) space
        
        Possible Approaches:
            1. Iterative Binary Search: Use two pointers to narrow range
            2. Recursive Binary Search: Divide range recursively
            3. Linear Scan: Check each element (not optimal)
        """
        pass

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums, target = [-1, 0, 3, 5, 9, 12], 9
        self.assertEqual(self.solution.binary_search(nums, target), 4)

    def test_target_not_found(self):
        nums, target = [-1, 0, 3, 5], 4
        self.assertEqual(self.solution.binary_search(nums, target), -1)

    def test_single_element(self):
        nums, target = [1], 1
        self.assertEqual(self.solution.binary_search(nums, target), 0)

    def test_two_elements(self):
        nums, target = [1, 2], 2
        self.assertEqual(self.solution.binary_search(nums, target), 1)

if __name__ == "__main__":
    unittest.main()