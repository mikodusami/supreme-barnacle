from typing import List
from collections import defaultdict
import unittest

def two_sum_indices(nums: List[int], target: int) -> List[int]:
    """
    Returns indices of two numbers that add up to target.
    
    Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Exactly one valid solution exists
    
    Args:
        nums: List of integers
        target: Integer target sum
    Returns:
        List[int]: Indices of the two numbers that add up to target
    """
    hesh = defaultdict(int)
    for key in range(0, len(nums)):
        compl = target - nums[key]
        if compl in hesh:
            return [hesh[compl], key]
        hesh[nums[key]] = key
    return []

class TestTwoSumIndices(unittest.TestCase):
    def test_example_case(self):
        """Test the example case: nums = [2, 7, 11, 15], target = 9"""
        self.assertEqual(sorted(two_sum_indices([2, 7, 11, 15], 9)), [0, 1])
    
    def test_negative_numbers(self):
        """Test case with negative numbers"""
        self.assertEqual(sorted(two_sum_indices([-1, -2, 3, 4], 2)), [0, 2])
    
    def test_two_elements(self):
        """Test case with minimum array length"""
        self.assertEqual(sorted(two_sum_indices([3, 3], 6)), [0, 1])
    
    def test_large_numbers(self):
        """Test case with large numbers"""
        self.assertEqual(sorted(two_sum_indices([10**9, -10**9], 0)), [0, 1])

# Possible Approaches:
# 1. Hash Map (Optimal): Store numbers and indices in a hash map, check for complement. Time: O(n), Space: O(n).
# 2. Brute Force: Check all pairs of numbers. Time: O(n^2), Space: O(1).
# 3. Sorting with Two-Pointer: Sort array and use two pointers, but requires index tracking. Time: O(n log n), Space: O(n).

if __name__ == '__main__':
    unittest.main()