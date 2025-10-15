from typing import List
import unittest

class Solution:
    def merge_sorted(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted lists nums1 and nums2 into nums1 in-place.
        nums1 has enough space to hold m+n elements.
        
        Args:
            nums1: List[int], sorted list with m elements and n extra spaces
            m: int, number of initialized elements in nums1
            nums2: List[int], sorted list with n elements
            n: int, number of elements in nums2
        Returns:
            None: Modifies nums1 in-place
        
        Constraints:
            - nums1.length == m + n
            - nums2.length == n
            - 0 <= m, n <= 200
            - Target: O(m+n) time, O(1) space
        """
        pass

class TestMergeSorted(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m, nums2, n = 3, [2, 5, 6], 3
        self.solution.merge_sorted(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_empty_nums1(self):
        nums1 = [0, 0, 0]
        m, nums2, n = 0, [1, 2, 3], 3
        self.solution.merge_sorted(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3])

    def test_empty_nums2(self):
        nums1 = [1, 2, 3]
        m, nums2, n = 3, [], 0
        self.solution.merge_sorted(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3])

    def test_single_element(self):
        nums1 = [1, 0]
        m, nums2, n = 1, [2], 1
        self.solution.merge_sorted(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2])

if __name__ == "__main__":
    unittest.main()