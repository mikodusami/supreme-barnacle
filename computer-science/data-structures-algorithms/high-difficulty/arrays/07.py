from typing import List
import unittest

def max_profit(prices: List[int]) -> int:
    """
    Finds the maximum profit from buying and selling a stock once.
    
    Constraints:
    - 1 <= prices.length <= 10^5
    - 0 <= prices[i] <= 10^4
    
    Args:
        prices: List of stock prices
    Returns:
        int: Maximum profit achievable, or 0 if no profit possible
    """
    pass
    max_profit = 0
    min_buying = prices[0]
    for i in range(0, len(prices)):
        min_buying = min(min_buying, prices[i])
        max_profit = max(max_profit, prices[i] - min_buying)
    return max_profit

class TestMaxProfit(unittest.TestCase):
    def test_example_case(self):
        """Test the example case: prices = [7, 1, 5, 3, 6, 4]"""
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
    
    def test_no_profit(self):
        """Test case where no profit is possible"""
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)
    
    def test_single_price(self):
        """Test case with single price"""
        self.assertEqual(max_profit([1]), 0)
    
    def test_two_prices_profit(self):
        """Test case with two prices and profit"""
        self.assertEqual(max_profit([1, 2]), 1)
    
    def test_two_prices_no_profit(self):
        """Test case with two prices and no profit"""
        self.assertEqual(max_profit([2, 1]), 0)

# Possible Approaches:
# 1. One-Pass (Optimal): Track minimum price and maximum profit while iterating. Time: O(n), Space: O(1).
# 2. Brute Force: Check all possible buy-sell pairs. Time: O(n^2), Space: O(1).
# 3. Kadane’s Algorithm Variant: Treat differences as profits and find max subarray sum. Time: O(n), Space: O(1).

if __name__ == '__main__':
    unittest.main()