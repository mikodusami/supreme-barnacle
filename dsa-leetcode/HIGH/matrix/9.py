from typing import List
import unittest

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Determines if a word exists in a 2D character board via adjacent cells.
        
        Args:
            board: List[List[str]], m×n board of characters
            word: str, target word to find
        Returns:
            bool: True if word exists, False otherwise
        
        Constraints:
            - 1 <= board.length, board[0].length <= 200
            - 1 <= word.length <= 10^3
            - Target: O(m*n*3^word.length) time, O(word.length) space
        
        Possible Approaches:
            1. DFS with Backtracking: Explore paths with marking
            2. BFS: Explore paths level by level (less common)
            3. Brute Force: Check all starting points exhaustively
        """
        pass

class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        self.assertTrue(self.solution.exist(board, word))

    def test_word_not_found(self):
        board = [["A", "B"], ["C", "D"]]
        word = "ABCDE"
        self.assertFalse(self.solution.exist(board, word))

    def test_single_character(self):
        board = [["A"]]
        word = "A"
        self.assertTrue(self.solution.exist(board, word))

    def test_same_letter_multiple_times(self):
        board = [["A", "A"], ["A", "A"]]
        word = "AAA"
        self.assertTrue(self.solution.exist(board, word))

if __name__ == "__main__":
    unittest.main()