from typing import List
import unittest

class Solution:
    def eval_rpn(self, tokens: List[str]) -> int:
        """
        Evaluates an arithmetic expression in Reverse Polish Notation (RPN).
        
        Args:
            tokens: List[str], RPN expression with integers and operators (+, -, *, /)
        Returns:
            int: Result of the expression
        
        Constraints:
            - 1 <= tokens.length <= 10^4
            - tokens[i] is a valid integer or operator
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Stack: Push operands, pop for operators
            2. Recursive Evaluation: Parse expression recursively (complex)
            3. Infix Conversion: Convert to infix then evaluate (not optimal)
        """
        pass

class TestEvalRPN(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(self.solution.eval_rpn(tokens), 9)

    def test_single_number(self):
        tokens = ["5"]
        self.assertEqual(self.solution.eval_rpn(tokens), 5)

    def test_subtraction(self):
        tokens = ["4", "3", "-"]
        self.assertEqual(self.solution.eval_rpn(tokens), 1)

    def test_complex_expression(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(self.solution.eval_rpn(tokens), 22)

if __name__ == "__main__":
    unittest.main()