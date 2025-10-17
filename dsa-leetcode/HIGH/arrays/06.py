from typing import List
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
    pass

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
    
    def test_odd_length_array(self):
        """Test case with odd-length array"""
        nums = [1, 2, 3, 4, 5]
        rotate_array(nums, 2)
        self.assertEqual(nums, [4, 5, 1, 2, 3])
    
    def test_even_length_array(self):
        """Test case with even-length array"""
        nums = [1, 2, 3, 4, 5, 6]
        rotate_array(nums, 3)
        self.assertEqual(nums, [4, 5, 6, 1, 2, 3])
    
    def test_k_maximum(self):
        """Test case with maximum k (10^5)"""
        nums = [1, 2, 3]
        rotate_array(nums, 100000)
        self.assertEqual(nums, [2, 3, 1])
    
    def test_mixed_numbers(self):
        """Test case with mixed positive and negative numbers"""
        nums = [-5, 0, 5, 10]
        rotate_array(nums, 3)
        self.assertEqual(nums, [0, 5, 10, -5])
    
    def test_small_array_large_k(self):
        """Test case with small array and very large k"""
        nums = [1, 2, 3]
        rotate_array(nums, 1000)
        self.assertEqual(nums, [1, 2, 3])
    
    def test_consecutive_numbers(self):
        """Test case with consecutive numbers"""
        nums = [1, 2, 3, 4, 5]
        rotate_array(nums, 4)
        self.assertEqual(nums, [2, 3, 4, 5, 1])
    
    def test_reverse_rotation_effect(self):
        """Test case where k causes near-full rotation"""
        nums = [1, 2, 3, 4, 5]
        rotate_array(nums, 4)
        self.assertEqual(nums, [2, 3, 4, 5, 1])
    
    def test_single_rotation_large_array(self):
        """Test case with large array and k = 1"""
        nums = list(range(100))
        rotate_array(nums, 1)
        self.assertEqual(nums, [99] + list(range(99)))
    
    def test_k_half_plus_one(self):
        """Test case with k equal to half length plus one"""
        nums = [1, 2, 3, 4, 5, 6]
        rotate_array(nums, 4)
        self.assertEqual(nums, [3, 4, 5, 6, 1, 2])
    
    def test_all_zeros(self):
        """Test case with all zeros"""
        nums = [0, 0, 0, 0]
        rotate_array(nums, 2)
        self.assertEqual(nums, [0, 0, 0, 0])
    
    def test_alternating_pattern(self):
        """Test case with alternating numbers"""
        nums = [1, 2, 1, 2]
        rotate_array(nums, 2)
        self.assertEqual(nums, [1, 2, 1, 2])
    
    def test_large_k_small_array(self):
        """Test case with very large k and small array"""
        nums = [1, 2]
        rotate_array(nums, 99999)
        self.assertEqual(nums, [2, 1])

# Possible Approaches:
# 1. Reverse Array (Optimal): Reverse entire array, then reverse first k and last n-k elements. Time: O(n), Space: O(1).
# 2. Cyclic Replacement: Move each element to its new position in cycles. Time: O(n), Space: O(1).
# 3. Extra Array: Create a new array to place elements in rotated positions, then copy back. Time: O(n), Space: O(n).

if __name__ == '__main__':
    unittest.main()