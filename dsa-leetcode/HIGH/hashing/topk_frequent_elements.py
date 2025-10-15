from typing import List
import unittest

class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        Returns the k most frequent elements in the list.
        
        Args:
            nums: List[int], list of integers
            k: int, number of frequent elements to return
        Returns:
            List[int]: k most frequent elements
        
        Constraints:
            - 1 <= nums.length <= 10^5
            - 1 <= k <= number of unique elements
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Hash Map + Bucket Sort: Group by frequency, select top k
            2. Hash Map + Heap: Use min-heap for top k frequencies
            3. Sorting: Sort by frequency (not optimal)
        """
        pass

class TestTopKFrequent(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums, k = [1, 1, 1, 2, 2, 3], 2
        self.assertEqual(sorted(self.solution.top_k_frequent(nums, k)), [1, 2])

    def test_single_element(self):
        nums, k = [1], 1
        self.assertEqual(self.solution.top_k_frequent(nums, k), [1])

    def test_all_same(self):
        nums, k = [1, 1, 1], 1
        self.assertEqual(self.solution.top_k_frequent(nums, k), [1])

    def test_k_equals_unique(self):
        nums, k = [1, 2, 3], 3
        self.assertEqual(sorted(self.solution.top_k_frequent(nums, k)), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()