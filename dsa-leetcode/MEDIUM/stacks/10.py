from typing import List
import unittest

class Solution:
    def largest_rectangle_area(self, heights: List[int]) -> int:
        """
        Finds the area of the largest rectangle in a histogram.
        
        Args:
            heights: List[int], heights of histogram bars
        Returns:
            int: Area of largest rectangle
        
        Constraints:
            - 1 <= heights.length <= 10^5
            - 0 <= heights[i] <= 10^4
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Monotonic Stack: Track increasing heights, compute areas
            2. Divide and Conquer: Find minimum height and recurse (not optimal)
            3. Brute Force: Check all possible rectangles (not optimal)
        """
        pass

class TestLargestRectangleArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        heights = [2, 1, 5, 6, 2, 3]
        self.assertEqual(self.solution.largest_rectangle_area(heights), 10)

    def test_single_bar(self):
        heights = [5]
        self.assertEqual(self.solution.largest_rectangle_area(heights), 5)

    def test_all_same_height(self):
        heights = [2, 2, 2]
        self.assertEqual(self.solution.largest_rectangle_area(heights), 6)

    def test_increasing_heights(self):
        heights = [1, 2, 3]
        self.assertEqual(self.solution.largest_rectangle_area(heights), 4)

if __name__ == "__main__":
    unittest.main()