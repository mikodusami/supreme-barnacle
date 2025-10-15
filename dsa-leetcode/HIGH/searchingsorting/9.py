from typing import List
import unittest

class Solution:
    def find_closest_elements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Finds the k closest integers to x in a sorted array, sorted in ascending order.
        
        Args:
            arr: List[int], sorted array of integers
            k: int, number of closest elements to find
            x: int, target value
        Returns:
            List[int]: k closest elements, sorted
        
        Constraints:
            - 1 <= k <= arr.length <= 10^5
            - arr is sorted in ascending order
            - Target: O(log n + k) time, O(1) space
        
        Possible Approaches:
            1. Binary Search: Find starting index, then expand window
            2. Two Pointers: Narrow down to k elements
            3. Heap: Use max-heap to track k closest (uses extra space)
        """
        pass

class TestFindClosestElements(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Assumed example: arr = [1,2,3,4,5], k=4, x=3
        arr, k, x = [1, 2, 3, 4, 5], 4, 3
        self.assertEqual(self.solution.find_closest_elements(arr, k, x), [1, 2, 3, 4])

    def test_single_element(self):
        arr, k, x = [1], 1, 1
        self.assertEqual(self.solution.find_closest_elements(arr, k, x), [1])

    def test_k_equals_length(self):
        arr, k, x = [1, 2, 3], 3, 2
        self.assertEqual(self.solution.find_closest_elements(arr, k, x), [1, 2, 3])

    def test_large_distance(self):
        arr, k, x = [1, 5, 10], 2, 3
        self.assertEqual(self.solution.find_closest_elements(arr, k, x), [1, 5])

if __name__ == "__main__":
    unittest.main()