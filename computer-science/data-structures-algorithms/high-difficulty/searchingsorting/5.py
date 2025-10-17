from typing import List
import unittest

class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        """
        Finds the k-th largest element in an unsorted array.
        
        Args:
            nums: List[int], unsorted array of integers
            k: int, k-th largest element to find
        Returns:
            int: k-th largest element
        
        Constraints:
            - 1 <= k <= nums.length <= 10^5
            - Target: O(n) average time, O(1) space
        
        Possible Approaches:
            1. QuickSelect: Partition and select k-th element
            2. Min-Heap: Maintain k largest elements
            3. Sorting: Sort array and select k-th (not optimal)
        """
        pass

class TestFindKthLargest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums, k = [3, 2, 1, 5, 6, 4], 2
        self.assertEqual(self.solution.find_kth_largest(nums, k), 5)

    def test_single_element(self):
        nums, k = [1], 1
        self.assertEqual(self.solution.find_kth_largest(nums, k), 1)

    def test_k_equals_length(self):
        nums, k = [3, 2, 1], 3
        self.assertEqual(self.solution.find_kth_largest(nums, k), 1)

    def test_duplicates(self):
        nums, k = [3, 3, 3, 2, 2], 2
        self.assertEqual(self.solution.find_kth_largest(nums, k), 3)

if __name__ == "__main__":
    unittest.main()