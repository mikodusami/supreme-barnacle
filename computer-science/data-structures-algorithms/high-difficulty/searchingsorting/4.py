from typing import List
import unittest

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges all overlapping intervals in a list of intervals.
        
        Args:
            intervals: List[List[int]], list of intervals [start, end]
        Returns:
            List[List[int]]: Merged intervals
        
        Constraints:
            - 1 <= intervals.length <= 10^4
            - Target: O(n log n) time, O(n) space
        
        Possible Approaches:
            1. Sort and Merge: Sort by start time, merge overlapping intervals
            2. Sweep Line: Use events to track interval overlaps
            3. Brute Force: Check all pairs for overlap (not optimal)
        """
        pass

class TestMerge(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        self.assertEqual(self.solution.merge(intervals), [[1, 6], [8, 10], [15, 18]])

    def test_single_interval(self):
        intervals = [[1, 4]]
        self.assertEqual(self.solution.merge(intervals), [[1, 4]])

    def test_all_overlapping(self):
        intervals = [[1, 4], [2, 3], [3, 5]]
        self.assertEqual(self.solution.merge(intervals), [[1, 5]])

    def test_no_overlap(self):
        intervals = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(self.solution.merge(intervals), [[1, 2], [3, 4], [5, 6]])

if __name__ == "__main__":
    unittest.main()