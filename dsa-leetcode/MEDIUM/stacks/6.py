import unittest

class Solution:
    def simplify_path(self, path: str) -> str:
        """
        Simplifies a Unix-style absolute path.
        
        Args:
            path: str, Unix-style path
        Returns:
            str: Canonical path
        
        Constraints:
            - 1 <= path.length <= 3000
            - path contains '/', '.', '..', and letters/numbers
            - Target: O(n) time, O(n) space
        
        Possible Approaches:
            1. Stack: Split path and process components
            2. String Manipulation: Parse and rebuild path
            3. Recursive Parsing: Handle components recursively (complex)
        """
        pass

class TestSimplifyPath(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        path = "/home//foo/."
        self.assertEqual(self.solution.simplify_path(path), "/home/foo")

    def test_root_path(self):
        path = "/"
        self.assertEqual(self.solution.simplify_path(path), "/")

    def test_parent_directory(self):
        path = "/a/./b/../../c/"
        self.assertEqual(self.solution.simplify_path(path), "/c")

    def test_multiple_slashes(self):
        path = "///"
        self.assertEqual(self.solution.simplify_path(path), "/")

if __name__ == "__main__":
    unittest.main()