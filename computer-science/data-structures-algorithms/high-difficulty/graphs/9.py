from typing import List
import unittest

class Solution:
    def ladder_length(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Finds the length of the shortest transformation sequence from beginWord to endWord.
        
        Args:
            beginWord: str, starting word
            endWord: str, target word
            wordList: List[str], list of valid words
        Returns:
            int: Length of shortest sequence, or 0 if none exists
        
        Constraints:
            - 1 <= beginWord.length <= 10
            - endWord.length == beginWord.length
            - 1 <= wordList.length <= 5000
            - Target: O(N * 26 * L) time, O(N) space (N: wordList length, L: word length)
        
        Possible Approaches:
            1. BFS: Treat words as nodes, edges as one-letter changes
            2. Bidirectional BFS: Search from both ends
            3. DFS: Explore all paths (not optimal)
        """
        pass

class TestLadderLength(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        beginWord, endWord, wordList = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(self.solution.ladder_length(beginWord, endWord, wordList), 5)

    def test_no_sequence(self):
        beginWord, endWord, wordList = "hit", "cog", ["hot", "dot", "dog"]
        self.assertEqual(self.solution.ladder_length(beginWord, endWord, wordList), 0)

    def test_single_step(self):
        beginWord, endWord, wordList = "hit", "hot", ["hot"]
        self.assertEqual(self.solution.ladder_length(beginWord, endWord, wordList), 2)

    def test_same_word(self):
        beginWord, endWord, wordList = "hit", "hit", ["hit"]
        self.assertEqual(self.solution.ladder_length(beginWord, endWord, wordList), 1)

if __name__ == "__main__":
    unittest.main()