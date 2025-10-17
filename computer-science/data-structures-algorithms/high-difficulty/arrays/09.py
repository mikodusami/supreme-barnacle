from typing import List
import unittest

def product_except_self(nums: List[int]) -> List[int]:
    """
    Returns an array where each element is the product of all other elements.
    
    Constraints:
    - 2 <= nums.length <= 10^5
    - -30 <= nums[i] <= 30
    - Product of any prefix or suffix fits in a 32-bit integer
    - Must run in O(n) time without using division
    
    Args:
        nums: List of integers
    Returns:
        List[int]: Array where each element is product of all others
    """
    pass

class TestProductExceptSelf(unittest.TestCase):
    def test_example_case(self):
        """Test the example case: nums = [1, 2, 3, 4]"""
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
    
    def test_two_elements(self):
        """Test case with minimum array length"""
        self.assertEqual(product_except_self([2, 3]), [3, 2])
    
    def test_with_zeros(self):
        """Test case with zeros"""
        self.assertEqual(product_except_self([1, 0, 3]), [0, 3, 0])
    
    def test_negative_numbers(self):
        """Test case with negative numbers"""
        self.assertEqual(product_except_self([-1, -2, -3]), [-6, -3, -2])
    
    def test_all_ones(self):
        """Test case with all ones"""
        self.assertEqual(product_except_self([1, 1, 1]), [1, 1, 1])

# Possible Approaches:
# 1. Left and Right Products (Optimal): Compute products of all elements to the left and right of each index. Time: O(n), Space: O(1) excluding output.
# 2. Division with Checks: Compute total product and divide by each element, handling zeros. Time: O(n), Space: O(1). Not allowed per constraints.
# 3. Brute Force: For each index, compute product of all other elements. Time: O(n^2), Space: O(1).

if __name__ == '__main__':
    unittest.main()