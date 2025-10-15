from typing import List
import unittest

class Solution:
    def max_area(self, height: List[int]) -> int:
        """
        Finds the maximum area of water that can be trapped between two vertical lines.
        
        Args:
            height: List[int], list of non-negative integers representing line heights
        Returns:
            int: Maximum area of water
        
        Constraints:
            - 2 <= height.length <= 10^5
            - 0 <= height[i] <= 10^4
            - Target: O(n) time, O(1) space
        """
        pass

class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        self.assertEqual(self.solution.max_area(height), 49)

    def test_two_lines(self):
        height = [1, 1]
        self.assertEqual(self.solution.max_area(height), 1)

    def test_equal_heights(self):
        height = [4, 4, 4, 4]
        self.assertEqual(self.solution.max_area(height), 12)

    def test_increasing_heights(self):
        height = [1, 2, 3, 4]
        self.assertEqual(self.solution.max_area(height), 6)

if __name__ == "__main__":
    unittest.main()