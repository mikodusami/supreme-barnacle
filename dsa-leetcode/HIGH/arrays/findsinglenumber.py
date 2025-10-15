from typing import List
import unittest

class Solution:
    def find_single_element(self, nums: List[int]) -> int:
        """
        Finds the single number in a non-empty list where every element appears twice except one.
        
        Args:
            nums: List[int], list of integers
        Returns:
            int: The single number that appears once
        
        Constraints:
            - 1 <= nums.length <= 3 * 10^4
            - Each element appears twice except for one
            - Target: O(n) time, O(1) space
        """
        pass

class TestFindSingleElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [4, 1, 2, 1, 2]
        self.assertEqual(self.solution.find_single_element(nums), 4)

    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.find_single_element(nums), 1)

    def test_three_elements(self):
        nums = [2, 2, 1]
        self.assertEqual(self.solution.find_single_element(nums), 1)

    def test_negative_numbers(self):
        nums = [-1, -1, 3, 3, -2]
        self.assertEqual(self.solution.find_single_element(nums), -2)

if __name__ == "__main__":
    unittest.main()