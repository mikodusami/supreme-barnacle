from typing import List
import unittest

class Solution:
    def can_finish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if all courses can be finished given prerequisites.
        
        Args:
            numCourses: int, number of courses (0 to numCourses-1)
            prerequisites: List[List[int]], list of [course, prerequisite] pairs
        Returns:
            bool: True if possible to finish all courses, False if cycle exists
        
        Constraints:
            - 1 <= numCourses <= 2000
            - 0 <= prerequisites.length <= 5000
            - Target: O(V + E) time, O(V) space (V: vertices, E: edges)
        
        Possible Approaches:
            1. DFS with Cycle Detection: Track visited nodes and recursion stack
            2. BFS with In-degree: Use Kahn's algorithm to detect cycles
            3. Union-Find: Detect cycles in graph (less common)
        """
        pass

class TestCanFinish(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        numCourses, prerequisites = 2, [[1, 0]]
        self.assertTrue(self.solution.can_finish(numCourses, prerequisites))

    def test_cycle(self):
        numCourses, prerequisites = 2, [[1, 0], [0, 1]]
        self.assertFalse(self.solution.can_finish(numCourses, prerequisites))

    def test_no_prerequisites(self):
        numCourses, prerequisites = 3, []
        self.assertTrue(self.solution.can_finish(numCourses, prerequisites))

    def test_single_course(self):
        numCourses, prerequisites = 1, []
        self.assertTrue(self.solution.can_finish(numCourses, prerequisites))

if __name__ == "__main__":
    unittest.main()