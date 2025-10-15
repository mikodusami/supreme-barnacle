from typing import List
import unittest

class Solution:
    def count_unique(self, nums: List[int]) -> int:
        """
        Returns the count of distinct elements in an unsorted list.
        
        Args:
            nums: List[int], unsorted list of integers
        Returns:
            int: Number of unique elements
        
        Constraints:
            - 0 <= nums.length <= 10^5
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Hash Set: Add elements to set, return size
            2. Sorting: Sort and count unique elements (not optimal)
            3. Brute Force: Compare each element with others (not optimal)
        """
        pass

class TestCountUnique(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 2, 3, 1, 4, 5, 4]
        self.assertEqual(self.solution.count_unique(nums), 5)

    def test_empty_list(self):
        nums = []
        self.assertEqual(self.solution.count_unique(nums), 0)

    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.count_unique(nums), 1)

    def test_all_same(self):
        nums = [2, 2, 2]
        self.assertEqual(self.solution.count_unique(nums), 1)

if __name__ == "__main__":
    unittest.main()