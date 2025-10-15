from typing import List
import unittest

class Solution:
    def total_fruit(self, fruits: List[int]) -> int:
        """
        Finds the maximum number of fruits that can be picked with at most two fruit types.
        
        Args:
            fruits: List[int], array of integers representing fruit types
        Returns:
            int: Maximum number of fruits that can be picked
        
        Constraints:
            - 1 <= fruits.length <= 10^5
            - Target: O(n) time, O(1) space
        
        Possible Approaches:
            1. Sliding Window: Track two fruit types, shrink when exceeding two
            2. Hash Map: Count fruit types in window
            3. Brute Force: Check all subarrays (not optimal)
        """
        pass

class TestTotalFruit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        fruits = [1, 2, 1, 3, 4, 3, 5]
        self.assertEqual(self.solution.total_fruit(fruits), 3)

    def test_single_fruit_type(self):
        fruits = [1, 1, 1]
        self.assertEqual(self.solution.total_fruit(fruits), 3)

    def test_two_fruit_types(self):
        fruits = [1, 2, 1, 2]
        self.assertEqual(self.solution.total_fruit(fruits), 4)

    def test_all_different(self):
        fruits = [1, 2, 3, 4]
        self.assertEqual(self.solution.total_fruit(fruits), 2)

if __name__ == "__main__":
    unittest.main()