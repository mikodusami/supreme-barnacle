from typing import List
from collections import defaultdict
import unittest

def rotate_array(nums: List[int], k: int) -> None:
    """
    Rotates the array to the right by k steps in-place.
    
    Constraints:
    - 1 <= nums.length <= 10^5
    - -2^31 <= nums[i] <= 2^31 - 1
    - 0 <= k <= 10^5
    
    Args:
        nums: List of integers
        k: Number of steps to rotate
    Returns:
        None: Modifies nums in-place
    """
    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    n = len(nums)
    if n <= 1:
        return
    k = k % n  # Normalize k
    if k == 0:
        return
    
    reverse(0, n - 1)      # Reverse entire array
    reverse(0, k - 1)      # Reverse first k elements
    reverse(k, n - 1)      # Reverse last n-k elements


class TestRotateArray(unittest.TestCase):
    def test_example_case(self):
        """Test the example case: nums = [1, 2, 3, 4, 5, 6, 7], k = 3"""
        nums = [1, 2, 3, 4, 5, 6, 7]
        rotate_array(nums, 3)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])
    
    def test_k_equals_length(self):
        """Test case where k equals array length"""
        nums = [1, 2, 3]
        rotate_array(nums, 3)
        self.assertEqual(nums, [1, 2, 3])
    
    def test_k_zero(self):
        """Test case where k is 0"""
        nums = [1, 2, 3]
        rotate_array(nums, 0)
        self.assertEqual(nums, [1, 2, 3])
    
    def test_single_element(self):
        """Test case with single element"""
        nums = [1]
        rotate_array(nums, 5)
        self.assertEqual(nums, [1])
    
    def test_large_k(self):
        """Test case with k larger than array length"""
        nums = [1, 2]
        rotate_array(nums, 5)
        self.assertEqual(nums, [2, 1])
    
    def test_negative_numbers(self):
        """Test case with negative numbers"""
        nums = [-1, -2, -3, -4]
        rotate_array(nums, 2)
        self.assertEqual(nums, [-3, -4, -1, -2])
    
    def test_maximum_length(self):
        """Test case with maximum length array (10^5) and small k"""
        nums = list(range(100000))
        rotate_array(nums, 1)
        self.assertEqual(nums, [99999] + list(range(99999)))
    
    def test_k_equals_half_length(self):
        """Test case where k equals half the array length"""
        nums = [1, 2, 3, 4]
        rotate_array(nums, 2)
        self.assertEqual(nums, [3, 4, 1, 2])
    
    def test_all_same_elements(self):
        """Test case with all identical elements"""
        nums = [5, 5, 5, 5]
        rotate_array(nums, 2)
        self.assertEqual(nums, [5, 5, 5, 5])
    
    def test_large_negative_numbers(self):
        """Test case with large negative numbers"""
        nums = [-2**31, -2**31 + 1, -2**31 + 2]
        rotate_array(nums, 1)
        self.assertEqual(nums, [-2**31 + 2, -2**31, -2**31 + 1])
    
    def test_large_positive_numbers(self):
        """Test case with large positive numbers"""
        nums = [2**31 - 1, 2**31 - 2, 2**31 - 3]
        rotate_array(nums, 1)
        self.assertEqual(nums, [2**31 - 3, 2**31 - 1, 2**31 - 2])
    
    def test_k_larger_than_length_multiple(self):
        """Test case with k as a multiple of array length plus extra"""
        nums = [1, 2, 3, 4]
        rotate_array(nums, 10)
        self.assertEqual(nums, [3, 4, 1, 2])
    
    def test_two_elements_k_one(self):
        """Test case with two elements and k = 1"""
        nums = [1, 2]
        rotate_array(nums, 1)
        self.assertEqual(nums, [2, 1])
    



# Possible Approaches:
# 1. Reverse Array (Optimal): Reverse entire array, then reverse first k and last n-k elements. Time: O(n), Space: O(1).
# 2. Cyclic Replacement: Move each element to its new position in cycles. Time: O(n), Space: O(1).
# 3. Extra Array: Create a new array to place elements in rotated positions, then copy back. Time: O(n), Space: O(n).

if __name__ == '__main__':
    unittest.main()