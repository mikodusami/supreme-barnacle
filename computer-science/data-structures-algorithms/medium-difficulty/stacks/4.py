from typing import List
import unittest

class Solution:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        """
        Returns the number of days to wait for a warmer temperature.
        
        Args:
            temperatures: List[int], list of daily temperatures
        Returns:
            List[int]: Days to wait for warmer temperature, 0 if none exists
        
        Constraints:
            - 1 <= temperatures.length <= 10^5
            - 30 <= temperatures[i] <= 100
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Monotonic Stack: Maintain stack of indices with increasing temperatures
            2. Brute Force: Check future days for each day (not optimal)
            3. Reverse Scan: Process array backwards (less intuitive)
        """
        pass

class TestDailyTemperatures(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        self.assertEqual(self.solution.daily_temperatures(temperatures), [1, 1, 4, 2, 1, 1, 0, 0])

    def test_single_day(self):
        temperatures = [50]
        self.assertEqual(self.solution.daily_temperatures(temperatures), [0])

    def test_decreasing_temperatures(self):
        temperatures = [50, 40, 30]
        self.assertEqual(self.solution.daily_temperatures(temperatures), [0, 0, 0])

    def test_increasing_temperatures(self):
        temperatures = [30, 40, 50]
        self.assertEqual(self.solution.daily_temperatures(temperatures), [1, 1, 0])

if __name__ == "__main__":
    unittest.main()