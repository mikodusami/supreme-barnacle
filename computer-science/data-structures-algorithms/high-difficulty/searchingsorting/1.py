from typing import List
import unittest

class Solution:
    def bubble_sort(self, arr: List[int]) -> List[int]:
        """
        Sorts an array of integers using the Bubble Sort algorithm.
        
        Args:
            arr: List[int], unsorted array of integers
        Returns:
            List[int]: Sorted array
        
        Constraints:
            - 0 <= arr.length <= 10^5
            - Target: O(n^2) time, O(1) space
        
        Possible Approaches:
            1. Standard Bubble Sort: Compare and swap adjacent elements
            2. Optimized Bubble Sort: Stop if no swaps are needed
            3. Recursive Bubble Sort: Recursively bubble largest element
        """
        pass

class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        arr = [5, 1, 4, 2, 8]
        self.assertEqual(self.solution.bubble_sort(arr), [1, 2, 4, 5, 8])

    def test_empty_array(self):
        arr = []
        self.assertEqual(self.solution.bubble_sort(arr), [])

    def test_single_element(self):
        arr = [1]
        self.assertEqual(self.solution.bubble_sort(arr), [1])

    def test_already_sorted(self):
        arr = [1, 2, 3]
        self.assertEqual(self.solution.bubble_sort(arr), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()