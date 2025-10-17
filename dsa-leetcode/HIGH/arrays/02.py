from typing import List
import unittest

def find_max_value(nums: List[int]) -> int:
    """
    Finds the largest integer value in a non-empty array.
    
    Constraints:
    - 1 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    
    Args:
        nums: Non-empty list of integers
    Returns:
        int: The largest integer in the array
    """
    max_number = nums[0]
    for i in range(0, len(nums)):
        max_number = max(max_number, nums[i])
    return max_number

class TestFindMaxValue(unittest.TestCase):
    def test_example_case(self):
        """Test the example case: nums = [5, -2, 10, 0, 8]"""
        self.assertEqual(find_max_value([5, -2, 10, 0, 8]), 10)
    
    def test_single_element(self):
        """Test case with single element"""
        self.assertEqual(find_max_value([3]), 3)
    
    def test_all_negative(self):
        """Test case with all negative numbers"""
        self.assertEqual(find_max_value([-1, -2, -3]), -1)
    
    def test_all_same(self):
        """Test case with all identical elements"""
        self.assertEqual(find_max_value([5, 5, 5]), 5)
    
    def test_large_numbers(self):
        """Test case with large numbers"""
        self.assertEqual(find_max_value([10**9, 0, -10**9]), 10**9)

# Possible Approaches:
# 1. Linear Scan (Optimal): Iterate through the array, tracking the maximum. Time: O(n), Space: O(1).
# 2. Using max() function: Python's built-in max() function. Time: O(n), Space: O(1).
# 3. Sorting: Sort the array and take the last element. Time: O(n log n), Space: O(1) or O(n) depending on sorting algorithm.

if __name__ == '__main__':
    unittest.main()