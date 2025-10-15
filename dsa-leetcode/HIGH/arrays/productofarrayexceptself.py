from typing import List
import unittest

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        """
        Returns an array where each element is the product of all other elements in nums.
        Cannot use division and must run in O(n) time.
        
        Args:
            nums: List[int], list of integers
        Returns:
            List[int]: Array of products excluding self
        
        Constraints:
            - 2 <= nums.length <= 10^5
            - Target: O(n) time, O(1) space (output array not counted)
        
        """
        pass

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(self.solution.product_except_self(nums), [24, 12, 8, 6])

    def test_two_elements(self):
        nums = [2, 3]
        self.assertEqual(self.solution.product_except_self(nums), [3, 2])

    def test_with_zero(self):
        nums = [1, 0, 3, 4]
        self.assertEqual(self.solution.product_except_self(nums), [0, 12, 0, 0])

    def test_negative_numbers(self):
        nums = [-1, -2, -3]
        self.assertEqual(self.solution.product_except_self(nums), [6, 3, 2])

if __name__ == "__main__":
    unittest.main()