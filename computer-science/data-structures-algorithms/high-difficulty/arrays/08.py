from typing import List
import unittest

def find_min(nums: List[int]) -> int:
    """
    Finds the minimum element in a rotated sorted array.
    
    Constraints:
    - 1 <= nums.length <= 5000
    - -5000 <= nums[i] <= 5000
    - All integers in nums are unique
    - nums is sorted and rotated
    
    Args:
        nums: Rotated sorted list of integers
    Returns:
        int: Minimum element in the array
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

class TestFindMin(unittest.TestCase):
    def test_example_case(self):
        """Test the example case: nums = [3, 4, 5, 1, 2]"""
        self.assertEqual(find_min([3, 4, 5, 1, 2]), 1)
    
    def test_no_rotation(self):
        """Test case with no rotation"""
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)
    
    def test_single_element(self):
        """Test case with single element"""
        self.assertEqual(find_min([1]), 1)
    
    def test_two_elements(self):
        """Test case with two elements"""
        self.assertEqual(find_min([2, 1]), 1)
    
    def test_all_elements_same_side(self):
        """Test case where all elements are on one side of rotation"""
        self.assertEqual(find_min([4, 5, 6, 7, 0]), 0)

# Possible Approaches:
# 1. Binary Search (Optimal): Use binary search to find the pivot point where minimum occurs. Time: O(log n), Space: O(1).
# 2. Linear Scan: Iterate through the array to find the minimum. Time: O(n), Space: O(1).
# 3. Find Pivot via Sorting: Sort the array and take the first element. Time: O(n log n), Space: O(1) or O(n).

if __name__ == '__main__':
    unittest.main()