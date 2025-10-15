from typing import List
import unittest

class Solution:
    def asteroid_collision(self, asteroids: List[int]) -> List[int]:
        """
        Simulates asteroid collisions and returns the final state.
        
        Args:
            asteroids: List[int], positive (right) or negative (left) integers
        Returns:
            List[int]: Final state of asteroids after collisions
        
        Constraints:
            - 2 <= asteroids.length <= 10^4
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Stack: Simulate collisions by pushing/popping asteroids
            2. Two Pointers: Process array in-place (complex)
            3. Simulation: Iterate and resolve collisions (less efficient)
        """
        pass

class TestAsteroidCollision(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        asteroids = [5, 10, -5]
        self.assertEqual(self.solution.asteroid_collision(asteroids), [5, 10])

    def test_all_same_direction(self):
        asteroids = [5, 10, 15]
        self.assertEqual(self.solution.asteroid_collision(asteroids), [5, 10, 15])

    def test_all_collide(self):
        asteroids = [10, -10]
        self.assertEqual(self.solution.asteroid_collision(asteroids), [])

    def test_multiple_collisions(self):
        asteroids = [-2, -1, 1, 2]
        self.assertEqual(self.solution.asteroid_collision(asteroids), [-2, -1, 1, 2])

if __name__ == "__main__":
    unittest.main()