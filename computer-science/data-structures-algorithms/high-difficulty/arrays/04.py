from typing import List
import unittest

def contains_duplicate(nums: List[int]) -> bool:
    """
    Determines if any value appears at least twice in the array.
    
    Constraints:
    - 1 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
    
    Args:
        nums: List of integers
    Returns:
        bool: True if any value appears at least twice, False otherwise
    """
    return len(nums) != len(set(nums))

class TestContainsDuplicate(unittest.TestCase):
    def test_example_case(self):
        """Test the example case: nums = [1, 2, 3, 1]"""
        self.assertTrue(contains_duplicate([1, 2, 3, 1]))
    
    def test_no_duplicates(self):
        """Test case with all unique elements"""
        self.assertFalse(contains_duplicate([1, 2, 3, 4]))
    
    def test_empty_array(self):
        """Test case with empty array"""
        self.assertFalse(contains_duplicate([]))
    
    def test_single_element(self):
        """Test case with single element"""
        self.assertFalse(contains_duplicate([1]))
    
    def test_all_duplicates(self):
        """Test case with all identical elements"""
        self.assertTrue(contains_duplicate([1, 1, 1]))

# Possible Approaches:
# 1. Hash Set (Optimal): Add elements to a set, check for duplicates. Time: O(n), Space: O(n).
# 2. Sorting: Sort the array and check adjacent elements. Time: O(n log n), Space: O(1) or O(n).
# 3. Brute Force: Compare each element with every other element. Time: O(n^2), Space: O(1).

if __name__ == '__main__':
    unittest.main()