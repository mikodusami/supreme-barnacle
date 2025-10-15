from typing import List
import unittest

class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in nums that sum to zero.
        
        Args:
            nums: List[int], list of integers
        Returns:
            List[List[int]]: List of unique triplets summing to zero
        
        Constraints:
            - 0 <= nums.length <= 3000
            - -10^5 <= nums[i] <= 10^5
            - Target: O(n^2) time, O(n) space
        """
        pass

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        self.assertEqual(sorted(self.solution.three_sum(nums)), sorted([[-1, -1, 2], [-1, 0, 1]]))

    def test_no_solution(self):
        nums = [1, 2, 3]
        self.assertEqual(self.solution.three_sum(nums), [])

    def test_empty_list(self):
        nums = []
        self.assertEqual(self.solution.three_sum(nums), [])

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        self.assertEqual(self.solution.three_sum(nums), [[0, 0, 0]])

    def test_single_triplet(self):
        nums = [-2, 0, 2]
        self.assertEqual(self.solution.three_sum(nums), [[-2, 0, 2]])

if __name__ == "__main__":
    unittest.main()