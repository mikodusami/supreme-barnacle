from typing import List
import unittest

def check_existence(arr: List[int], target: int) -> bool:
    """
    Determines if the target value exists in the array.
    
    Constraints:
    - 1 <= arr.length <= 10^4
    - -10^9 <= arr[i], target <= 10^9
    
    Args:
        arr: List of integers
        target: Integer to find in the array
    Returns:
        bool: True if target exists in arr, False otherwise
    """

    # To Determine If The Target Value Is In The Array
    # What Does This Mean: This means that there is a value in the array that we need to find. The array alwasy has one element so we do not have to ensure the array is populated however the value may not exist in the array. 
    # Sub Problems:
    # -- Finding a value in the array:
    # == psba: linearly iterate through each element in the array until we find the number
    # == psba: use the two pointer approach to start in the front and the back until we find the number (o log n)

    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

    pass

class TestCheckExistence(unittest.TestCase):
    def test_example_case(self):
        """Test the example case: arr = [3, 1, 4, 1, 5, 9], target = 4"""
        self.assertTrue(check_existence([3, 1, 4, 1, 5, 9], 4))
    
    def test_target_not_found(self):
        """Test case where target is not in the array"""
        self.assertFalse(check_existence([1, 2, 3, 5], 4))
    
    def test_empty_array(self):
        """Test case with empty array"""
        self.assertFalse(check_existence([], 1))
    
    def test_single_element_found(self):
        """Test case with single element array where target exists"""
        self.assertTrue(check_existence([1], 1))
    
    def test_single_element_not_found(self):
        """Test case with single element array where target does not exist"""
        self.assertFalse(check_existence([1], 2))
    
    def test_negative_numbers(self):
        """Test case with negative numbers"""
        self.assertTrue(check_existence([-1, -2, 0, 3], -2))

# Possible Approaches:
# 1. Linear Search (Optimal): Iterate through the array and check each element for equality with target. Time: O(n), Space: O(1).
# 2. Set Conversion: Convert array to a set and use 'in' operator. Time: O(n) for conversion, O(1) for lookup, Space: O(n).
# 3. Binary Search (if sorted): If array is sorted, use binary search. Time: O(log n), Space: O(1). Not applicable here as array is not guaranteed sorted.

if __name__ == '__main__':
    unittest.main()