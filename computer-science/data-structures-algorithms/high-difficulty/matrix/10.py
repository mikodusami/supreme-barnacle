from typing import List
import unittest

class Solution:
    def solve_sudoku(self, board: List[List[str]]) -> None:
        """
        Solves a 9×9 Sudoku puzzle by modifying the board in-place.
        
        Args:
            board: List[List[str]], 9×9 board with digits '1'-'9' or '.'
        Returns:
            None: Modifies board in-place
        
        Constraints:
            - board.length == board[0].length == 9
            - board[i][j] is '1'-'9' or '.'
            - Target: O(9^m) time (m: empty cells), O(1) space
        
        Possible Approaches:
            1. Backtracking: Try digits and validate constraints
            2. Constraint Propagation: Reduce possibilities before backtracking
            3. Brute Force: Try all combinations (not optimal)
        """
        pass

class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        expected = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
        ]
        self.solution.solve_sudoku(board)
        self.assertEqual(board, expected)

    def test_empty_board(self):
        board = [["." for _ in range(9)] for _ in range(9)]
        self.solution.solve_sudoku(board)
        self.assertTrue(self.is_valid_sudoku(board))

    def test_single_cell(self):
        board = [["1" if i == 0 and j == 0 else "." for j in range(9)] for i in range(9)]
        self.solution.solve_sudoku(board)
        self.assertTrue(self.is_valid_sudoku(board))

    def is_valid_sudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                val = board[i][j]
                if val in rows[i] or val in cols[j] or val in boxes[(i//3)*3 + j//3]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[(i//3)*3 + j//3].add(val)
        return True

if __name__ == "__main__":
    unittest.main()