from typing import List
import unittest

def first_missing_positive(nums: List[int]) -> int:
    """
    Finds the smallest positive integer missing from the array.
    
    Constraints:
    - 1 <= nums.length <= 10^5
    - -2^31 <= nums[i] <= 2^31 - 1
    - Must run in O(n) time with constant extra space
    
    Args:
        nums: List of integers
    Returns:
        int: Smallest positive integer missing
    """
    pass

class TestFirstMissingPositive(unittest.TestCase):
    def test_example_case(self):
        """Test the example case: nums = [1, 2, 0]"""
        self.assertEqual(first_missing_positive([1, 2, 0]), 3)
    
    def test_negative_numbers(self):
        """Test case with negative numbers"""
        self.assertEqual(first_missing_positive([-1, -2, 0]), 1)
    
    def test_consecutive_numbers(self):
        """Test case with consecutive positive numbers"""
        self.assertEqual(first_missing_positive([1, 2, 3]), 4)
    
    def test_duplicates(self):
        """Test case with duplicates"""
        self.assertEqual(first_missing_positive([3, 4, -1, 1, 1]), 2)
    
    def test_single_element(self):
        """Test case with single element"""
        self.assertEqual(first_missing_positive([1]), 2)
    
    def test_empty_positive(self):
        """Test case with no positive numbers"""
        self.assertEqual(first_missing_positive([0, -1, -2]), 1)

# Possible Approaches:
# 1. Index as Hash (Optimal): Use the array itself to mark presence of numbers by indexing, ignoring non-positive and out-of-range numbers. Time: O(n), Space: O(1).
# 2. Hash Set: Store positive numbers in a set, check for missing numbers starting from 1. Time: O(n), Space: O(n). Not allowed due to space constraint.
# 3. Sorting: Sort the array, then scan for missing positive number. Time: O(n log n), Space: O(1). Not allowed due to time constraint.

if __name__ == '__main__':
    unittest.main()