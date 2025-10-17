from typing import List
import unittest

def remove_duplicates(nums: List[int]) -> int:
    """
    Removes duplicates from a sorted array in-place and returns the new length.
    
    Constraints:
    - 0 <= nums.length <= 3 * 10^4
    - -100 <= nums[i] <= 100
    - nums is sorted in ascending order
    
    Args:
        nums: Sorted list of integers
    Returns:
        int: Length of array after removing duplicates
    """
    if not nums:
        return 0
    
    # Two SUBS:
    #1. Removing Duplicates In Place
    # pointer that only points to unique elements, so as we iterate through the array, we replace the number at the pointer with the current element. The pointer only shifts forward once we have found a number that does not equal the previous
    #2. Calculating Length
    left = 0
    for right in range(1, len(nums)):
        if nums[right] != nums[left] and nums[right] > nums[left]:
            left += 1
            nums[left] = nums[right]
    return left + 1
    #  nums = [1, 1, 2, 2, 1, 1, 2, 2]
class TestRemoveDuplicates(unittest.TestCase):
    def test_example_case(self):
        """Test the example case: nums = [1, 1, 2, 2, 3, 4, 4]"""
        nums = [1, 1, 2, 2, 3, 4, 4]
        k = remove_duplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 3, 4])
    
    def test_empty_array(self):
        """Test case with empty array"""
        nums = []
        k = remove_duplicates(nums)
        self.assertEqual(k, 0)
        self.assertEqual(nums, [])
    
    def test_no_duplicates(self):
        """Test case with no duplicates"""
        nums = [1, 2, 3]
        k = remove_duplicates(nums)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [1, 2, 3])
    
    def test_all_duplicates(self):
        """Test case with all identical elements"""
        nums = [1, 1, 1, 1]
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])
    
    def test_single_element(self):
        """Test case with single element"""
        nums = [1]
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])
    
    def test_negative_numbers(self):
        """Test case with negative numbers and duplicates"""
        nums = [-3, -3, -2, -1, -1, 0]
        k = remove_duplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [-3, -2, -1, 0])
    
    def test_maximum_length(self):
        """Test case with maximum length array (3 * 10^4) with no duplicates"""
        nums = list(range(30000))
        k = remove_duplicates(nums)
        self.assertEqual(k, 30000)
        self.assertEqual(nums[:k], list(range(30000)))
    
    def test_maximum_duplicates(self):
        """Test case with maximum length array all duplicates"""
        nums = [1] * 30000
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])
    
    def test_mixed_positive_negative(self):
        """Test case with mixed positive and negative numbers"""
        nums = [-2, -2, 0, 0, 1, 2, 2]
        k = remove_duplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [-2, 0, 1, 2])
    
    def test_all_zeros(self):
        """Test case with all zeros"""
        nums = [0, 0, 0, 0, 0]
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [0])
    
    def test_boundary_values(self):
        """Test case with boundary values (-100 and 100)"""
        nums = [-100, -100, 0, 100, 100]
        k = remove_duplicates(nums)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [-100, 0, 100])
    
    def test_two_elements_same(self):
        """Test case with two identical elements"""
        nums = [5, 5]
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [5])
    
    def test_two_elements_different(self):
        """Test case with two different elements"""
        nums = [1, 2]
        k = remove_duplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])
    
    def test_consecutive_duplicates(self):
        """Test case with multiple consecutive duplicates"""
        nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
        k = remove_duplicates(nums)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [1, 2, 3])
    
    def test_large_numbers(self):
        """Test case with large numbers within constraints"""
        nums = [90, 90, 95, 95, 100, 100]
        k = remove_duplicates(nums)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [90, 95, 100])
    
    def test_single_duplicate_pairs(self):
        """Test case with each number duplicated once"""
        nums = [1, 1, 2, 2, 3, 3, 4, 4]
        k = remove_duplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 3, 4])
    
    def test_alternating_pattern(self):
        """Test case with alternating duplicates"""
        nums = [1, 1, 2, 2, 1, 1, 2, 2]
        k = remove_duplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])
    
    def test_long_sequence_duplicates(self):
        """Test case with long sequence of same number"""
        nums = [1] * 100 + [2] * 100
        k = remove_duplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])
    
    def test_minimum_values(self):
        """Test case with minimum value (-100) repeated"""
        nums = [-100] * 50
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [-100])
    
    def test_maximum_values(self):
        """Test case with maximum value (100) repeated"""
        nums = [100] * 50
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [100])
    
    def test_mixed_duplicates(self):
        """Test case with mixed duplicates and unique elements"""
        nums = [-50, -50, 0, 0, 0, 50, 50, 75]
        k = remove_duplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [-50, 0, 50, 75])
    
    def test_sorted_unique_long(self):
        """Test case with long sorted array with unique elements"""
        nums = list(range(-50, 51))
        k = remove_duplicates(nums)
        self.assertEqual(k, 101)
        self.assertEqual(nums[:k], list(range(-50, 51)))
    
    def test_single_duplicate_long(self):
        """Test case with one number repeated many times"""
        nums = [0] * 1000
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [0])
    
    def test_random_sorted_with_duplicates(self):
        """Test case with random sorted numbers with duplicates"""
        nums = [-10, -10, -5, 0, 0, 5, 5, 10]
        k = remove_duplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [-10, -5, 0, 5, 10])
    
    def test_edge_case_alternating(self):
        """Test case with alternating unique and duplicate elements"""
        nums = [-1, -1, 0, 1, 1, 2]
        k = remove_duplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [-1, 0, 1, 2])

# Possible Approaches:
# 1. Two-Pointer (Optimal): Use a slow pointer for unique elements and a fast pointer to scan. Time: O(n), Space: O(1).
# 2. Set Conversion: Convert to set to remove duplicates, then overwrite array. Time: O(n), Space: O(n).
# 3. Brute Force: For each element, check subsequent elements for duplicates and shift. Time: O(n^2), Space: O(1).

if __name__ == '__main__':
    unittest.main()