from typing import List
import unittest

class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive sequence in an unsorted list.
        
        Args:
            nums: List[int], unsorted list of integers
        Returns:
            int: Length of the longest consecutive sequence
        
        Constraints:
            - 0 <= nums.length <= 10^5
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Hash Set: Store numbers, check for sequence starts
            2. Sorting: Sort and count consecutive sequences (not O(n))
            3. Union-Find: Group consecutive numbers (complex)
        """
        pass

class TestLongestConsecutive(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [100, 4, 200, 1, 3, 2]
        self.assertEqual(self.solution.longest_consecutive(nums), 4)

    def test_empty_list(self):
        nums = []
        self.assertEqual(self.solution.longest_consecutive(nums), 0)

    def test_no_sequence(self):
        nums = [1, 3, 5, 7]
        self.assertEqual(self.solution.longest_consecutive(nums), 1)

    def test_all_same(self):
        nums = [2, 2, 2]
        self.assertEqual(self.solution.longest_consecutive(nums), 1)

if __name__ == "__main__":
    unittest.main()