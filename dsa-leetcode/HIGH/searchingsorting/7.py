from typing import List
import unittest

class Solution:
    def find_peak_element(self, nums: List[int]) -> int:
        """
        Finds the index of a peak element (strictly greater than neighbors).
        
        Args:
            nums: List[int], array of integers
        Returns:
            int: Index of any peak element
        
        Constraints:
            - 1 <= nums.length <= 1000
            - Assume nums[-1] = nums[n] = -∞
            - Target: O(log n) time, O(1) space
        
        Possible Approaches:
            1. Binary Search: Compare middle element with neighbors, search promising half
            2. Linear Scan: Check each element against neighbors (not optimal)
            3. Recursive Binary Search: Divide and conquer approach
        """
        pass

class TestFindPeakElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 1, 3, 5, 6, 4]
        self.assertEqual(self.solution.find_peak_element(nums), 5)

    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.find_peak_element(nums), 0)

    def test_two_elements(self):
        nums = [1, 2]
        self.assertEqual(self.solution.find_peak_element(nums), 1)

    def test_multiple_peaks(self):
        nums = [1, 3, 2, 4, 1]
        self.assertIn(self.solution.find_peak_element(nums), [1, 3])

if __name__ == "__main__":
    unittest.main()