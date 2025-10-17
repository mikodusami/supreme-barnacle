from typing import List
import unittest

def findMaxAverage(nums: List[int], k: int) -> float:
    # Constraints:
    # - 1 <= k <= n <= 10^5
    # - -10^4 <= nums[i] <= 10^4
    # - Return the maximum average of any contiguous subarray of size k
    # - Time complexity target: O(n)
    # - Space complexity target: O(1)
    
    pass

class TestMaxAverageSubarray(unittest.TestCase):
    def test_example_case(self):
        # Example: nums = [1, 12, -5, -6, 50, 3], k = 4 -> 12.75
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        self.assertAlmostEqual(findMaxAverage(nums, k), 12.75)

    def test_single_element(self):
        # Edge case: Single element array with k=1
        nums = [5]
        k = 1
        self.assertAlmostEqual(findMaxAverage(nums, k), 5.0)

    def test_all_negative(self):
        # Edge case: All negative numbers
        nums = [-1, -2, -3, -4]
        k = 2
        self.assertAlmostEqual(findMaxAverage(nums, k), -1.5)

    def test_k_equals_n(self):
        # Edge case: k equals array length
        nums = [1, 2, 3, 4]
        k = 4
        self.assertAlmostEqual(findMaxAverage(nums, k), 2.5)

# Possible Approaches:
# 1. Brute Force: Compute the sum of every possible subarray of size k and find the maximum average.
#    - Time: O(n*k), Space: O(1)
# 2. Sliding Window (Optimal): Use a sliding window of size k to compute the sum, updating by subtracting the leftmost element and adding the next element.
#    - Time: O(n), Space: O(1)
# 3. Prefix Sum: Use prefix sums to compute subarray sums in O(1) after O(n) preprocessing, but still iterate over all possible windows.
#    - Time: O(n), Space: O(n)
# Optimal Approach: Sliding Window, as it achieves O(n) time and O(1) space, meeting the problem's constraints efficiently.

if __name__ == '__main__':
    unittest.main()